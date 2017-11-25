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
cost_factor = 0.01875 #$/km
initial_cost = 30680
sql_script = ('SELECT date, distance FROM camry_distance')
sql = cur.execute(sql_script)

#Step1. Loop through camry_distance and store reading in the list reading_a
for row in sql:
    reading_a.append(row)

conn.commit()
conn.close()

#Step2. Connect to the wallflower pico database
conn_pico = sqlite3.connect('wallflower_db.sqlite')
cur_pico = conn_pico.cursor()
total_cost = 0

for i in reading_a:
    reading_date = str(i[0])
    reading_distance = i[1]
    reading_cost = reading_distance * cost_factor
    total_cost = total_cost + reading_cost
    print "the total cost are"
    print total_cost
    interval_start_time_text = '11:59'
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
    sql_script = 'INSERT INTO' + '[' + 'local.analysis-b.stm-analysis-b' + ']' + '(timestamp, value) VALUES ' + '(' + '?' + ',' + '?' + ')'
    cur_pico.execute (sql_script, (datetime_unix,total_cost))

conn_pico.commit()
