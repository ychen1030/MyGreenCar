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

'''
 In this example, we will create an object (test-object) and a stream
 (test-stream) and populate it with random values.
'''
import requests
import json
import random
import time
import datetime

base = 'http://127.0.0.1:5000'
network_id = 'local'
header = {}


query = {
    'object-name': 'Test Object'
}
endpoint = '/networks/'+network_id+'/objects/test-object'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 201:
    print('Create object test-object: ok')
else:
    print('Create object test-object: error')
    print( response.text )

query = {
    'stream-name': 'Test Stream',
    'points-type': 'i' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/test-object/streams/test-stream'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
    print('Create stream test-stream: ok')
else:
    print('Create stream test-stream: error')
    print( response.text )

#Part 2 --> send arduino sensor data to webpage
"""
    Simple program structure

"""

import time
import serial

serial_port_name = '/dev/cu.usbserial-DN01JNRK'
ser = serial.Serial(serial_port_name, 9600, timeout = 1)

delay = 1*10 # Delay in seconds

# Run once at the start
def setup():
    try:
        print "Setup"
    except:
        print "Setup Error"

# Run continuously forever
def loop():
    # 100 ms delay
    time.sleep(0.1)
    if ser.inWaiting() > 0:
        try:
            x = float(ser.readline())
            print "HEEEYYYYY HEEEEREEEE -----> Received:", x
            print "Type:", type(x)
            return x

        except:
            print "Error"
    time.sleep(.1)
    return x

def delayed_loop():
    print "Delayed Loop"
# Run once at the end
def close():
    try:
        print "Close Serial Port"
        ser.close()

    except:
        print "Close Error"

# Program Structure
def main():
    y = 0
    # Call setup function
    setup()
    # Set start time
    nextLoop = time.time()
    print ("----------------------------------------------")
    print("Start the wholeeee loop")
    endpoint = '/networks/local/objects/test-object/streams/test-stream/points'
    while(True):
        # Try loop() and delayed_loop()
        print ("I am in the first step")
        try:
            y = int(loop())
            if time.time() > nextLoop:
                # If next loop time has passed...
                    nextLoop = time.time() + delay
                    delayed_loop()
        except KeyboardInterrupt:
            break

        except:
            # Catch all errors
            print "Unexpected error."

        print ('Your y value came out to be',y)

        query = {
            'points-value': y,
            'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        }
        print ("I made it to the second step and query is ",query)
        response = requests.request('POST', base + endpoint, params=query, headers=header )
        print ("I made it to the third step and your post is ", response)
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Update test-stream points: ok')
        else:
            print( 'Update test-stream points: error')
            print( response.text )
        print ("I made it to the fourth step and.... to sleep for 10s")
        time.sleep(10)
    # Call close function
    close()

# Run the program
main()
