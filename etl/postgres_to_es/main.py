"""Starts ETL process to load data from postgres to elasticsearch."""

from time import sleep

from config import Settings
from etl import ETL

if __name__ == '__main__':
    while True:
        etl = ETL()
        for batch in etl.extract():
            data = etl.transform(batch)
            etl.load(data)
        sleep(Settings().UPDATE_TIME)
