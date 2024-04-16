from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import numpy as np
import datetime
import sqlite3
import shutup
import pathlib

from database_utils import get_table_names

shutup.please()


def scrape_forex():
    forex_url = "https://www.tradingview.com/markets/currencies/rates-asia/"
    prefix = "https://www.tradingview.com/symbols/ECONOMICS-"

    chrome_options = Options()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(forex_url)

    try:
        # wait for the web content to load
        target = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"/symbols/USDJPY")]'))
        )

        more_button = driver.find_element(By.XPATH, '//*[@id="js-category-content"]/div[2]/div/div[4]/button/span')
        more_button.click()

        table = driver.find_element(By.XPATH,
                                    '//*[@id="js-category-content"]/div[2]/div/div[4]/div[2]/div[2]/div/div/table/tbody')
        rows = table.find_elements(By.XPATH, 'tr')
        filtered_rows = [row for row in rows if 'CNY' in row.get_attribute('data-rowkey')]

        forex_pairs = [row.get_attribute('data-rowkey') for row in filtered_rows]
        attributes = ['Symbol', 'Price', 'PercentChange', 'Change', 'Bid', 'Ask', 'High', 'Low', 'TechRating']
        value_df = pd.DataFrame(np.zeros((len(forex_pairs), len(attributes))), columns=attributes)
        for i in range(len(filtered_rows)):
            row = filtered_rows[i]
            symbol = row.get_attribute('data-rowkey')
            value_df.loc[i, 'Symbol'] = symbol
            tds = row.find_elements(By.XPATH, 'td')
            for j in range(1, len(tds) - 1):
                td = tds[j]
                try:
                    span_tag = td.find_element(By.XPATH, 'span')
                except:
                    span_tag = None
                if span_tag is not None:
                    span = span_tag.text
                    value_df.loc[i, attributes[j]] = span
                else:
                    value_df.loc[i, attributes[j]] = td.text
            last_td = tds[-1]
            value_df.loc[i, attributes[-1]] = last_td.find_element(By.XPATH, 'div').text
        return value_df

    finally:
        # close window
        driver.quit()


def update_indicator():
    attributes = ['Symbol', 'Price', 'PercentChange', 'Change', 'Bid', 'Ask', 'High', 'Low', 'TechRating']
    forex_data = scrape_forex()
    today = str(datetime.datetime.now().date()).replace('-', '_')
    cwd = pathlib.Path(__file__).parent.resolve()
    database_dir = str(cwd).replace('python_service', 'database')
    conn = sqlite3.connect(database_dir + r'\forex.db')
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS T{today} ({', '.join(x + ' TEXT' for x in attributes)})")
    forex_data.to_sql(con=conn, name='T' + today, index=False, if_exists='append')


if __name__ == '__main__':
    cwd = pathlib.Path(__file__).parent.resolve()
    database_dir = str(cwd).replace('python_service', 'database')
    tables = get_table_names(database_dir + r'\forex.db')
    if 'T' + str(datetime.datetime.now().date()).replace('-', '_') not in tables:
        update_indicator()
