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

country_suffix = ["US", "CN", "EU", "JP", "DE", "GB", "FR", "RU", "CA", "IT", "AU"]
indicator_suffix = ['GDP', 'POP', 'GDPYY', 'INTR', 'IRYY', 'UR', 'CAG', 'GDG']


def scrape_indicator():
    indicator_url = "https://www.tradingview.com/markets/world-economy/indicators/"
    prefix = "https://www.tradingview.com/symbols/ECONOMICS-"

    chrome_options = Options()
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(indicator_url)

    try:
        # wait for the web content to load
        target = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[contains(@href,"ECONOMICS-USGDP")]'))
        )

        # init value dataframe
        value_df = pd.DataFrame(np.zeros((len(indicator_suffix), len(country_suffix) + 1)),
                                columns=['indicator'] + country_suffix)
        value_df['indicator'] = pd.Series(indicator_suffix)

        for country in country_suffix:
            for indicator in indicator_suffix:
                indicator_path = f'//a[contains(@href,"ECONOMICS-{country + indicator}")]'
                indicator_value = driver.find_element(By.XPATH, indicator_path).find_element(By.CSS_SELECTOR,
                                                                                             "span").text
                value_df.loc[indicator_suffix.index(indicator), country] = indicator_value

        return value_df

    finally:
        # close window
        driver.quit()


def update_indicator():
    econ_indicators = scrape_indicator()
    today = str(datetime.datetime.now().date()).replace('-', '_')
    cwd = pathlib.Path(__file__).parent.resolve()
    database_dir = str(cwd).replace('python_service', 'database')
    conn = sqlite3.connect(database_dir + r'\econ_indicators.db')
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS T{today} (indicator TEXT, {', '.join(x + ' TEXT' for x in country_suffix)})")
    econ_indicators.to_sql(con=conn, name='T' + today, index=False, if_exists='append')


if __name__ == '__main__':
    tables = get_table_names('../database/econ_indicators.db')
    if 'T' + str(datetime.datetime.now().date()).replace('-', '_') not in tables:
        update_indicator()