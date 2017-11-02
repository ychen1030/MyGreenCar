#####################################################################################
#
#  Copyright (c) 2016 Eric Burger, Wallflower.cc
#
#  MIT License (MIT)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
#####################################################################################
#
# '''
#  In this example, we will create an object (test-object) and a stream
#  (test-stream) and populate it with random values.
# '''
import requests
import json
import random
import time
import datetime
import ReceiveDatatest
import serial
import syslog


#Part1 write data to the arduino
serial_port_name = '/dev/cu.usbserial-DN01JNRK'
ard = serial.Serial(serial_port_name, 9600, timeout = 1)
i=0
#Part2 Connect to the server
base = 'http://127.0.0.1:5000'
network_id = 'local'
header = {}


#Part2 Get data from server

#Create connection with Test Object
query_report = {
    'object-name' : 'Report State'
}

endpoint_report = '/networks/'+network_id+'/objects/test-object/streams/test-stream'
i = 0
while True:
    response_report = requests.request('GET', base + endpoint_report, params=query_report, headers=header, timeout=120 )
    resp_report = json.loads( response_report.text )
    length_retrieved = len(resp_report["points"])
    print json.dumps(resp_report, indent=4)
    last_value = resp_report["points"][length_retrieved-1]["value"]
    print last_value
    if last_value >= 70:
        setTempCar1 = '1'
        setTemp1 = str(setTempCar1)
        print ("Python value sent: ")
        print (setTemp1)
        ard.write(setTemp1)
    elif last_value <= 70:
        setTempCar2 = '0'
        setTemp2 = str(setTempCar2)
        print ("Python value sent: ")
        print (setTemp2)
        ard.write(setTemp2)
    else:
        print ("Bad Data")
    i += 1
    print i
    time.sleep(10)
