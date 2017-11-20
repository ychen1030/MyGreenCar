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

conn = sqlite3.connect('astrodek.sqlite')
cur = conn.cursor()

d = os.getcwd()

d1 = os.path.join(d,'Data')
fname = os.path.join(d1,'main_data.csv')
# f = open(fname,"r")

# Read the main_data.csv file and create the relevant tables to store data in
with open(fname, 'rU') as main_data_csv:
    main_data_reader = csv.DictReader(main_data_csv)
    try:
        for line in main_data_reader:
            #Get the specific data from the csv file and store in variables
            reading_id = line['id']
            reading_file = line['file']
            car_type = line['type']


            #Create scripts to drop tables and create tables
            drop_tables = ("DROP TABLE IF EXISTS " +
                            "[" + str(car_type) +"]" )

            create_tables = ("CREATE TABLE IF NOT EXISTS " +
                            "[" + str(car_type) + "]" +
                            """ (id INTEGER PRIMARY KEY UNIQUE,
                            time TIME,
                            date DATE,
                            latitude INTEGER,
                            longitude INTEGER,
                            latitudedeg INTEGER,
                            longitudedeg INTEGER,
                            speed INTEGER,
                            gpsangle INTEGER,
                            altitud INTEGER)""")

            #Run the drop tables and create tables scripts
            cur.execute(drop_tables)

            cur.execute(create_tables)

    except:
        print "error posting data, try again"

conn.commit()
