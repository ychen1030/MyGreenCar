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
cost_factor = 0.0602083333333333 #$/km
initial_cost = 23495
days_year = 365
manufacture_emissions_camry = 7000000 #gCO2e
manufacture_emissions_leaf = 9400000 #gCO2e
dates = ['16/11/2018','16/11/2019','16/11/2020','16/11/2021','16/11/2022','16/11/2023','16/11/2024','16/11/2025','16/11/2026','16/11/2027']

#Step1 --> obtain emissions from Nissan Leaf
sql_script_user = 'SELECT timestamp,value FROM ' + '[' + 'local.sensorreading.stm-sensor' + ']'
sql_user = cur.execute (sql_script_user)
for row in sql_user:
    reading_a.append(row)

days_data = len(reading_a)

for i in reading_a: #output the latest emissions reading
    total_emissions_user = i[1]
# print total_emissions_user

#Step2 --> obtain emissions from Nissan Leaf
sql_script_leaf = 'SELECT timestamp,value FROM ' + '[' + 'local.analysis-a.stm-analysis-a' + ']'
sql_leaf = cur.execute (sql_script_leaf)
for row in sql_leaf:
    reading_b.append(row)

days_leaf = len(reading_b)
count = 0
for i in reading_b: #output the latest emissions reading
    total_emissions_leaf = i[1]
    if count == 0:
        first_date = i[0]
    count += 1


print total_emissions_leaf
print first_date
#Step3 --> obtain avg daily savings
avg_savings = (total_emissions_user - total_emissions_leaf)/days_data
print avg_savings
count = 0
total_savings = 0
#Step4 --> obtain 10yr savings
for i in range(10):
    if count == 0:
        year_savings = (manufacture_emissions_camry - manufacture_emissions_leaf)
    else:
        year_savings = days_year * avg_savings
    total_savings += year_savings
    interval_start_time_text = '11:59'
    time_text = dates[i] +' '+ interval_start_time_text
    count += 1
    print total_savings
    try:
        datetime_test = (datetime.strptime(time_text, '%d-%m-%Y  %H:%M'))
        datetime_unix = dtt.datetime.strptime(time_text,'%d-%m-%Y %H:%M')
    except:
        datetime_test = (datetime.strptime(time_text, '%d/%m/%Y %H:%M'))
        datetime_unix = dtt.datetime.strptime(time_text,'%d/%m/%Y %H:%M')

    sql_script_savings = 'INSERT INTO' + '[' + 'local.analysis-c.stm-analysis-c' + ']' + '(timestamp, value) VALUES ' + '(' + '?' + ',' + '?' + ')'
    cur.execute (sql_script_savings, (datetime_unix,total_savings))


conn.commit()
