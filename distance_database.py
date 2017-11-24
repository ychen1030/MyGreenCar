import sqlite3
import datetime
import time
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, HourLocator, MinuteLocator
import lat_long

conn = sqlite3.connect('astrodek.sqlite')
cur = conn.cursor()


reading_a = []
reading_b = []

sql_script = ('SELECT date, distance FROM camry_clean')
sql = cur.execute(sql_script)

# Step 1.   Insert all the dates and distances into a list
for row in sql:
    reading_a.append(row)

# Step 2.   Read list from step one and inser the dates into de camry_distance
#           database
for i in reading_a:
    reading_date = i[0]
    reading_distance = i[1]
    sql_script = 'INSERT OR IGNORE INTO camry_distance (date) VALUES (?)'
    cur.execute (sql_script, (reading_date,))

#Step3.     With unique reading dates, now save them in list reading_b
sql_script_distance = ('SELECT date FROM camry_distance')
sql = cur.execute(sql_script_distance)

for row in sql:
    reading_b.append(row)

#Step4.     Loop through the list with the date readings.
#           Loop through the camry_clean database and obtain dates, readings
#           Compare the dates and if dates coincide, then add the distance
#           readings.

#Step4.1 --> unique date readings loop
for i in reading_b:
    reading_date = i[0]
    print reading_date

#   Step4.2 --> dates and readings from camry_clean
    sql_script_distance = ('SELECT date, distance FROM camry_clean')
    # Obtain all values from readings. Gives you back two values
    # [0] = date, value [1] = distance
    sql_distance = cur.execute(sql_script_distance)
    # Set an empty count for total_distance
    total_distance = 0

#   Step4.3 --> Loop over all the readings and only add up those with the same
#               date
    for row in sql_distance:
        current_date = row[0]
        current_distance = float(row[1])
        if current_date == reading_date:
            total_distance = total_distance + current_distance
        else:
            total_distance = total_distance
    print total_distance
    sql_script = 'UPDATE camry_distance SET distance = ? WHERE date = ' + '(' + '?' + ')'
    cur.execute (sql_script, (total_distance,reading_date))

conn.commit()
