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
                latitude_v = str(i[' Latitude'])
                longitude_v = str(i[' Longitude'])
                latitudedeg_v = str(i[' Latitudedegree'])
                longitudedeg_v = str(i[' Longitudedegree'])
                speed_v = float(i[' Speed'])
                gpsangle_v = str(i[' GPSangle'])
                altitud_v = str(i[' Altitude'])


                #Cleanup data from start of measurement
                time_v_clean = (re.findall('\S+[0-9]',time_v))
                date_v_clean = re.findall('\S+[0-9]',date_v)
                latitude_v_clean = re.findall('\S+[0-9]',latitude_v)
                longitude_v_clean = re.findall('\S+[0-9]',longitude_v)
                latitudedeg_v_clean = re.findall('\S+[a-zA-Z0-9_.-]',latitudedeg_v)
                longitudedeg_v_clean = re.findall('\S+[a-zA-Z0-9_.-]',longitudedeg_v)

                if speed_v != 0:
                    speed_v_clean = speed_v

                else:
                    speed_v_clean = 0.00

                gpsangle_v_clean = gpsangle_v
                altitud_v_clean = altitud_v

                # Cleanup data required for date and timestamp
                # time_text = date_v_clean[0] + ' ' + time_v_clean[0]
                # try:
                #     datetime_test = (datetime.strptime(time_text, '%d/%m/%Y  %H:%M:%S'))
                #     ut = (datetime_test - dtt.datetime(1970, 1, 1)).total_seconds()
                # except:
                #     try:
                #         datetime_test = (datetime.strptime(time_text, '%d/%m/%Y %H:%M.%S'))
                #         ut = (datetime_test - dtt.datetime(1970, 1, 1)).total_seconds()
                #     except:
                #         datetime_test = (datetime.strptime(time_text, ' %d/%m/%Y  %H:%M.%S'))
                #         ut = (datetime_test - dtt.datetime(1970, 1, 1)).total_seconds()


                sql_script = 'INSERT INTO' + '[' + str(car_type) + ']' + '(date, latitude, longitude, latitudedeg, longitudedeg, speed, gpsangle, altitud) VALUES ' + '(' + '?' + ',' + '?' + ',' + '?' + ',' + '?' + ',' + '?' + ',' + '?' + ',' + '?' + ',' + '?' + ')'

                cur.execute(sql_script,(date_v_clean[0], latitude_v_clean[0],longitude_v_clean[0], latitudedeg_v_clean[0], longitudedeg_v_clean[0], speed_v_clean, gpsangle_v_clean, altitud_v_clean))

conn.commit()
