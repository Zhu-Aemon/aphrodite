"""
get commodity price data and store it in a database for further usage
"""
import os

import pandas as pd
import sqlite3
import requests
import datetime

API_KEY = 'Y252S9HNUHX9W3SX'


def get_commodity_price_alphaV(symbol, interval='daily'):
    """
    get commodity price of a given symbol
    :param interval: the interval of data. Available: daily, weekly, monthly
    :param symbol: the commodity symbol, like 'WTI'. Available symbols: WTI, BRENT, NATURAL_GAS, COPPER, ALUMINUM, WHEAT,
    CORN, COTTON, SUGAR, COFFEE, ALL_COMMODITIES
    :return: json format of data
    """
    url = f'https://www.alphavantage.co/query?function={symbol}&interval={interval}&apikey={API_KEY}'
    # url = 'https://www.alphavantage.co/query?function=COPPER&interval=monthly&apikey=demo'
    r = requests.get(url)
    data = r.json()
    return data


def init_data(symbol):
    conn = sqlite3.connect('database/commodity.db')
    cur = conn.cursor()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {symbol} (date DATE, value REAL)
    """)
    conn.commit()
    return


def check_table_is_empty(symbol: str, database='commodity.db'):
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


def get_latest_date(symbol: str, database='commodity.db'):
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
        # print(cur.fetchall()[0][0])
        # return cur.fetchall()[0][0]
        return datetime.datetime.strptime(cur.fetchall()[0][0][:10], '%Y-%m-%d')


def daily_update(symbol):
    init_data(symbol=symbol)
    data = get_commodity_price_alphaV(symbol=symbol)
    price_df = pd.DataFrame(data['data'])
    price_df['date'] = pd.to_datetime(price_df['date'])
    conn = sqlite3.connect('database/commodity.db')
    # write data to sqlite3 database
    if check_table_is_empty(symbol=symbol):
        price_df.to_sql(name=symbol, con=conn, if_exists='append', index=False)
    else:
        latest_date = get_latest_date(symbol=symbol)
        try:
            price_df[price_df['date'] > latest_date].to_sql(name=symbol, con=conn, if_exists='append', index=False)
        except TypeError:
            print(f'the return of function `get_latest_date` {latest_date} is not a datetime object')


if __name__ == "__main__":
    symbol_list = ['WTI', 'BRENT', 'NATURAL_GAS', 'COPPER', 'ALUMINUM', 'WHEAT', 'CORN', 'COTTON', 'SUGAR',
                   'COFFEE', 'ALL_COMMODITIES']
    for symbol_iter in symbol_list:
        if (not check_table_is_empty(symbol=symbol_iter)) and get_latest_date(symbol=symbol_iter).date() == datetime.date.today():
            continue
        daily_update(symbol=symbol_iter)
