"""Starts ETL process to load data from postgres to elasticsearch."""

from time import sleep

from config import UPDATE_TIME
from etl import ETL

while True:
    etl = ETL()
    for batch in etl.extract():
        data = etl.transform(batch)
        etl.load(data)
    sleep(UPDATE_TIME)
