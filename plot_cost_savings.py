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

conn = sqlite3.connect('wallflower_db.sqlite')
cur = conn.cursor()

reading_a = []
reading_b = []
reading_c = []
r = .06 #6% rate of return
cost_factor = 0.0602083333333333 #$/km
initial_cost_camry = 23495
initial_cost_leaf = 30680
initial_cost_total = initial_cost_camry - initial_cost_leaf
days_year = 365
dates = ['15/11/17','30/11/17','16/11/2018','16/11/2019','16/11/2020','16/11/2021','16/11/2022','16/11/2023','16/11/2024','16/11/2025','16/11/2026','16/11/2027']

#Step1 --> obtain cost from Nissan Leaf and store it in reading_a
sql_script_leaf = 'SELECT timestamp,value FROM ' + '[' + 'local.analysis-b.stm-analysis-b' + ']'
sql_leaf = cur.execute (sql_script_leaf)
for row in sql_leaf:
    reading_a.append(row)

days_data = len(reading_a)

for i in reading_a: #output the latest cost reading
    total_cost_user = i[1]


#Step2 --> obtain cost from user car
sql_script_user = 'SELECT timestamp,value FROM ' + '[' + 'local.buttonstate.stm-button' + ']'
sql_user = cur.execute (sql_script_user)
for row in sql_user:
    reading_b.append(row)

days_leaf = len(reading_b)
count = 0

for i in reading_b: #output the latest cost reading
    total_cost_leaf = i[1]
    if count == 0:
        first_date = i[0]
    count += 1


#Step3 --> obtain avg daily savings
avg_savings = (total_cost_user - total_cost_leaf)/days_data
print total_cost_user
print total_cost_leaf
print avg_savings
count = 0
#Step4 --> obtain 10yr savings
total_savings = 0
for i in range(10):
    if count == 0:
        interval_initial_time_text = '11:59'
        time_text = dates[0] +' '+ interval_initial_time_text
        try:
            datetime_test = (datetime.strptime(time_text, '%d/%m/%y  %H:%M'))
            datetime_unix = dtt.datetime.strptime(time_text,'%d/%m/%y %H:%M')
        except:
            datetime_test = (datetime.strptime(time_text, '%d/%m/%Y %H:%M'))
            datetime_unix = dtt.datetime.strptime(time_text,'%d/%m/%Y %H:%M')
        sql_script_initial = 'INSERT INTO' + '[' + 'local.camry-cost.stm-camry-cost' + ']' + '(timestamp, value) VALUES ' + '(' + '?' + ',' + '?' + ')'
        cur.execute (sql_script_initial, (datetime_unix,initial_cost_total))
        print datetime_unix, initial_cost_total
    elif count == 1:
        year_savings = (days_leaf * avg_savings)/((1+r)**count)
        initial_cost_total -= year_savings
        interval_start_time_text = '11:59'
        time_text = dates[count] +' '+ interval_start_time_text

        try:
            datetime_test = (datetime.strptime(time_text, '%d/%m/%Y  %H:%M'))
            datetime_unix = dtt.datetime.strptime(time_text,'%d/%m/%Y %H:%M')
        except:
            datetime_test = (datetime.strptime(time_text, '%d/%m/%y %H:%M'))
            datetime_unix = dtt.datetime.strptime(time_text,'%d/%m/%y %H:%M')

        print datetime_unix, initial_cost_total
        sql_script_savings = 'INSERT INTO' + '[' + 'local.camry-cost.stm-camry-cost' + ']' + '(timestamp, value) VALUES ' + '(' + '?' + ',' + '?' + ')'
        cur.execute (sql_script_savings, (datetime_unix,initial_cost_total))

    else:
        year_savings = (days_year * avg_savings)/((1+r)**count)
        initial_cost_total -= year_savings
        interval_start_time_text = '11:59'
        time_text = dates[count] +' '+ interval_start_time_text

        try:
            datetime_test = (datetime.strptime(time_text, '%d/%m/%Y  %H:%M'))
            datetime_unix = dtt.datetime.strptime(time_text,'%d/%m/%Y %H:%M')
        except:
            datetime_test = (datetime.strptime(time_text, '%d/%m/%y %H:%M'))
            datetime_unix = dtt.datetime.strptime(time_text,'%d/%m/%y %H:%M')

        print datetime_unix, initial_cost_total
        sql_script_savings = 'INSERT INTO' + '[' + 'local.camry-cost.stm-camry-cost' + ']' + '(timestamp, value) VALUES ' + '(' + '?' + ',' + '?' + ')'
        cur.execute (sql_script_savings, (datetime_unix,initial_cost_total))
    count += 1


conn.commit()
