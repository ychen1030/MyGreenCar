import sqlite3
import datetime
import time
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, HourLocator, MinuteLocator
import lat_long
from datetime import datetime
import datetime as dtt

conn = sqlite3.connect('astrodek.sqlite')
cur = conn.cursor()

reading_a = []
reading_b = []

sql_script = ('SELECT date, distance FROM camry_distance')
sql = cur.execute(sql_script)

for row in sql:
    reading_a.append(row)

conn.commit()
conn.close()

conn_pico = sqlite3.connect('wallflower_db.sqlite')
cur_pico = conn_pico.cursor()

for i in reading_a:
    reading_date = str(i[0])
    reading_distance = i[1]
    interval_start_time_text = '11:59'
    print type(reading_distance)

    time_text = reading_date +' '+ interval_start_time_text
    try:
        datetime_test = (datetime.strptime(time_text, '%d-%m-%Y  %H:%M'))
        datetime_unix = dtt.datetime.strptime(time_text,'%d-%m-%Y %H:%M')
        # ut = (datetime_test - dtt.datetime(1970, 1, 1)).total_seconds()
    except:
        datetime_test = (datetime.strptime(time_text, '%d/%m/%Y %H:%M'))
        datetime_unix = dtt.datetime.strptime(time_text,'%d/%m/%Y %H:%M')
        # ut = (datetime_test - dtt.datetime(1970, 1, 1)).total_seconds()
    print datetime_unix
    # sql_script = '(INSERT INTO [local.test-object.test-stream] (timestamp,value) VALUES (?,?)))'
    sql_script = 'INSERT INTO' + '[' + 'local.test-object.test-stream' + ']' + '(timestamp, value) VALUES ' + '(' + '?' + ',' + '?' + ')'
    cur_pico.execute (sql_script, (datetime_unix,reading_distance))

conn_pico.commit()
