# Before you run this program.
# This program is intended to read the csv files have been:
# 1) Downloaded from the utility API website as csv files
# 2) Saved in the Data folder
# 3) The name convention nees to be [address] + @ + [type of bill]
# 4) The file main_data.csv needs to be populated with the information regarding the files

# Once the data is stored with the correct naming convention and the main_data.csv
# has been populated
# 1) This program will go over all the files,
# 2) Create a table inside the astrodek.sqlite database for each house/apt
# 3) Store .......... in the data base

import csv
import sqlite3
import re
import dateutil.parser as parser
import os
import pytz
import time
from datetime import datetime
import datetime as dtt


conn = sqlite3.connect('astrodek.sqlite')
cur = conn.cursor()

d = os.getcwd()

d1 = os.path.join(d,'Data')
fname = os.path.join(d1,'main_data.csv')



with open(fname, 'rU') as main_data_csv:
    main_data_reader = csv.DictReader(main_data_csv)
    for i in main_data_reader:
        file_name = i['file']
        car_type = i['type']
        file_name_path = i['file']+'.csv'
        car_file = os.path.join(d1,file_name_path)
        with open(car_file, 'rU') as car_data:
            main_data_reader = csv.DictReader(car_data)
            for i in main_data_reader:
                time_v = str(i['Time'])
                date_v = str(i[' Date'])
                # latitude_v = float(i['Latitude'])
                # longitude_v = float(i['Longitude'])
                # latitudedeg_v = float(i['Latitudedeg'])
                # longitudedeg_v = float(i['Longitudedeg'])
                # speed_v = float(i['Speed'])
                # gpsangle_v = float(i['GPSangle'])
                # altitud_v = float(i['Altitud'])
                print time_v, date_v
                # #Cleanup data from start of measurement
                # interval_start_date = re.findall('[0-9]\S+ ',interval_start)
                # interval_start_date_text = str(interval_start_date[0])
                # interval_start_time = re.findall('\s.+', interval_start)
                # interval_start_time_text = str(interval_start_time[0])
                # #Cleanup data from end of measurement
                # interval_end_date = re.findall('[0-9]\S+ ',interval_end)
                # interval_end_date_text = str(interval_end_date[0])
                # interval_end_time = re.findall('\s.+', interval_end)
                # interval_end_time_text = str(interval_end_time[0])
                #
                # #Cleanup data required for date and timestamp
                # time_text = interval_start_date_text + interval_start_time_text
                # try:
                #     datetime_test = (datetime.strptime(time_text, '%m-%d-%y  %H:%M'))
                #     # datetime_unix = dtt.datetime.strptime(datetime_test,'%Y-%m-%d %H:%M:%S')
                #     ut = (datetime_test - dtt.datetime(1970, 1, 1)).total_seconds()
                # except:
                #     datetime_test = (datetime.strptime(time_text, '%m/%d/%y  %H:%M'))
                #     # datetime_unix = dtt.datetime.strptime(datetime_test,'%Y-%m-%d %H:%M:%S')
                #     ut = (datetime_test - dtt.datetime(1970, 1, 1)).total_seconds()
                #
                # sql_script = 'INSERT OR IGNORE INTO' + '[' + str(house_name) + ']' + '(timestamp, interval_start_time, interval_start_date, interval_end_time, interval_end_date, interval_kW) VALUES ' + '(' + '?' + ',' + '?' +',' + '?' + ',' + '?' + ',' + '?' + ',' + '?' + ')'
                # cur.execute(sql_script,(ut, interval_start_time_text, interval_start_date_text,interval_end_time_text,interval_start_date_text,interval_kW))
                #

conn.commit()
