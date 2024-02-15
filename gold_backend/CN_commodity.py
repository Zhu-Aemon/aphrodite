"""
Get Chinese Commodity data and store it in a database for further reference
"""
import datetime

import pandas as pd
import sqlite3

import akshare as ak
import shutup

shutup.please()


def init_data_cn(symbol):
    """
    init sqlite3 database sheet for this symbol
    :param symbol: the symbol of the future, for example 'V0'
    :return: nothing
    """
    conn = sqlite3.connect('database/cn_commodity.db')
    cur = conn.cursor()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {symbol} (date DATE, open REAL, high REAL, low REAL, close REAL, volume REAL, inventory REAL)
    """)
    conn.commit()
    return


def get_cn_commodity_data(symbol):
    """
    get the daily data of the given CN commodity using akshare API
    :param symbol: the symbol of the future, for example 'V0'
    :return: nothing
    """
    raw_data = ak.futures_main_sina(symbol)
    raw_data.rename(columns={'日期': 'date', '开盘价': 'open', '收盘价': 'close', '最高价': 'high', '最低价': 'low', '成交量': 'volume', '持仓量': 'inventory'}, inplace=True)
    raw_data['date'] = pd.to_datetime(raw_data['date'])
    raw_data.drop(columns=['动态结算价'], inplace=True)
    return raw_data


def check_table_is_empty_cn(symbol: str, database='database/cn_commodity.db'):
    """
    check if the given table is empty
    :param symbol: commodity symbol
    :param database: database filename
    :return: True or False. True for symbol sheet to be empty and False otherwise
    """
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    with conn:
        cur.execute(f"SELECT * FROM {symbol}")
        return not bool(cur.fetchall())


def get_latest_date_cn(symbol: str, database='database/cn_commodity.db'):
    """
    get the latest date of the given database sheet
    :param symbol: commodity symbol
    :param database: database filename
    :return: the latest date, if empty return None
    """
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    with conn:
        cur.execute(f"SELECT * FROM {symbol}")
        # return cur.fetchall()[0][0]
        return datetime.datetime.strptime(cur.fetchall()[-1][0][:10], '%Y-%m-%d').date()


def cn_daily_update(symbol):
    """
    run a daily update on a CN symbol to keep the data of the CN future in our database up to date
    :param symbol: the symbol of a given CN future, for example 'V0'
    :return: nothing
    """
    init_data_cn(symbol=symbol)
    data = get_cn_commodity_data(symbol=symbol)
    data.rename(columns={'日期': 'date', '开盘价': 'open', '收盘价': 'close', '最高价': 'high', '最低价': 'low', '成交量': 'volume', '持仓量': 'inventory'}, inplace=True)
    data['date'] = pd.to_datetime(data['date']).dt.date
    try:
        data.drop(columns=['动态结算价'], inplace=True)
    except KeyError:
        pass
        # print(data)
    price_df = data
    conn = sqlite3.connect('database/cn_commodity.db')
    # write data to sqlite3 database
    if check_table_is_empty_cn(symbol=symbol):
        price_df.to_sql(name=symbol, con=conn, if_exists='append', index=False)
    else:
        latest_date = get_latest_date_cn(symbol=symbol)
        try:
            price_df[price_df['date'] > latest_date].to_sql(name=symbol, con=conn, if_exists='append', index=False)
        except TypeError as e:
            print(f'the return of function `get_latest_date` {latest_date} is not a datetime object, error: {e}')


def get_all_futures():
    """
    get all CN future symbols
    """
    conn = sqlite3.connect('database/all_cn_futures.db')
    cur = conn.cursor()
    with conn:
        cur.execute("CREATE TABLE IF NOT EXISTS futures (symbol TEXT, exchange TEXT, name TEXT)")
        cn_futures = ak.futures_display_main_sina()
        cn_futures.to_sql(name='futures', con=conn, index=False, if_exists='append')


if __name__ == '__main__':
    if check_table_is_empty_cn(symbol='futures', database='database/all_cn_futures.db'):
        get_all_futures()
    all_futures_conn = sqlite3.connect('database/all_cn_futures.db')
    all_futures_cur = all_futures_conn.cursor()
    with all_futures_conn:
        all_futures_cur.execute("SELECT symbol FROM futures")
        all_futures_data = all_futures_cur.fetchall()
        all_futures_data = [x[0] for x in all_futures_data]
    for symbol_iter in all_futures_data:
        iter_conn = sqlite3.connect('database/cn_commodity.db')
        iter_cur = iter_conn.cursor()
        with iter_conn:
            iter_cur.execute(f"CREATE TABLE IF NOT EXISTS {symbol_iter} (date DATE, open REAL, high REAL, low REAL, close REAL, volume REAL, inventory REAL)")
        if (not check_table_is_empty_cn(symbol=symbol_iter)) and get_latest_date_cn(symbol=symbol_iter) == datetime.datetime.now().date():
            continue
        cn_daily_update(symbol=symbol_iter)
        print(f'finished {symbol_iter}')
