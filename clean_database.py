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

sql_script = ('SELECT id, latitude, longitude, date, latitudedeg, longitudedeg FROM camry')
sql = cur.execute(sql_script)

for row in sql:
    reading_a.append(row)

for i in reading_a:
    reading_id = int(i[0])
    reading_latitude = i[1]
    reading_longitude = i[2]
    reading_date = i[3]
    reading_latitudedeg = i[4]
    reading_longitudedeg = i[5]
    previous_reading_id = reading_id - 1

    # Obtain the previous value for latitude reading to compute distance

    # try:
    #     cur.execute('SELECT latitude FROM camry WHERE id = ? ', (previous_reading_id, ))
    #     previous_latitude = cur.fetchone()[0]
    #
    # except:
    #     previous_latitude = reading_latitude
    #
    # try:
    #     cur.execute('SELECT longitude FROM camry WHERE id = ? ', (previous_reading_id, ))
    #     previous_longitude = cur.fetchone()[0]
    #
    # except:
    #     previous_longitude = reading_longitude

    # Obtain the previous deg readings for lat and long to compute distance
    try:
        cur.execute('SELECT latitudedeg FROM camry WHERE id = ? ', (previous_reading_id, ))
        previous_latitudedeg = cur.fetchone()[0]

    except:
        previous_latitudedeg = reading_latitudedeg

    try:
        cur.execute('SELECT longitudedeg FROM camry WHERE id = ? ', (previous_reading_id, ))
        previous_longitudedeg = cur.fetchone()[0]

    except:
        previous_longitudedeg = reading_longitudedeg

    try:
        cur.execute('SELECT date FROM camry WHERE id = ? ', (previous_reading_id, ))
        previous_date = cur.fetchone()[0]

    except:
        previous_date = "NA"

    # print "latitudedeg"
    # print reading_latitudedeg
    # print "longitude"
    # print reading_longitudedeg
    # print "previous_latitude"
    # print previous_latitude
    # print "previous reading"
    # print previous_longitude

    if reading_latitudedeg == previous_latitudedeg and reading_longitudedeg == previous_longitudedeg:
        distance = 0

    elif previous_date != reading_date:
        distance = 0

    else:
        distance = lat_long.distance(reading_latitudedeg, reading_longitudedeg, previous_latitudedeg, previous_longitudedeg)
    sql_script = 'INSERT OR IGNORE INTO camry_clean (date, distance) VALUES ' + '(' + '?' + ',' + '?' + ')'
    cur.execute (sql_script, (reading_date, distance))

conn.commit()
