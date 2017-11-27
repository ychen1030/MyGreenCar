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

emission_factor = 267 #gCO2/km
sql_script = ('SELECT date, distance FROM camry_distance')
sql = cur.execute(sql_script)

#Step1. Loop through camry_distance and store reading in the list reading_a
for row in sql:
    reading_a.append(row)

conn.commit()
conn.close()

#
# #Step2. Connect to the wallflower pico database
conn_pico = sqlite3.connect('wallflower_db.sqlite')
cur_pico = conn_pico.cursor()
accumulated_emissions = list()
total_emissions = 0
for i in reading_a:
    reading_date = str(i[0])
    reading_distance = i[1]
    reading_emissions = reading_distance * emission_factor
    accumulated_emissions.append(reading_emissions)

    # print "the total emissions are"
    # print total_emissions

    total_emissions = sum (accumulated_emissions)
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
    # sql_script = '(INSERT INTO [local.test-object.test-stream] (timestamp,value) VALUES (?,?)))'
    sql_script = 'INSERT INTO' + '[' + 'local.sensorreading.stm-sensor' + ']' + '(timestamp, value) VALUES ' + '(' + '?' + ',' + '?' + ')'
    cur_pico.execute (sql_script, (datetime_unix,total_emissions))

conn_pico.commit()
