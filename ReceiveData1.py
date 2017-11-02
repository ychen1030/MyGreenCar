"""
    Simple program structure

"""
import time
import serial
import stringToInt

serial_port_name = '/dev/cu.usbserial-DN01JNRK'
ser = serial.Serial(serial_port_name, 9600, timeout = 1)
PhotoResistor = list()
ButtonState = list()
delay = 1*10 # Delay in seconds

# Run once at the start
def setup():
    try:
        print "Setup"
    except:
        print "Setup Error"

def loop():
    # 100 ms delay
    time.sleep(0.1)
    if ser.inWaiting() > 0:
        try:
            x = ser.readline()
            y = list(x)
            test = stringToInt.BigList(y)
            print test
            if y[0] == "#":
                ButtonState.append(y[1])
                print ButtonState.len()

            else:
                print "made it here"
                # numba = stringToInt.BigList(y)
                # PhotoResistor.append(numba)

        except:
            print "Error"
            time.sleep(1)

        return

# Run continuously forever
# with a delay between calls
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
    # Call setup function
    setup()
    # Set start time
    nextLoop = time.time()
    while(True):
        # Try loop() and delayed_loop()
        try:
            loop()
            if time.time() > nextLoop:
                # If next loop time has passed...
                nextLoop = time.time() + delay
                delayed_loop()
        except KeyboardInterrupt:
            # If user enters "Ctrl + C", break while loop
            break
        except:
            # Catch all errors
            print "Unexpected error."
        #ButtonState
        time.sleep(2)
        print (PhotoResistor)
    # Call close function
    close()

loop()
