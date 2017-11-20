from time import sleep
from hedgehog.client import connect

# Welcome to Hedghog's textual programming environment!

# Lines starting with the "#" charakter are comments and ignored during the
# program execution. To make them effective, simple remove the preceding "#".
# Command can be used to document your code.

# The comments in this file provide a quick introduction with writing Python
# programs for the Hedgehog Robotics Controller. If you are already familiar
# with Python and Hedgehog specific commands, you can savely ignore them.
# That being said, lets get started!

# Connect to the Hedgehog controller.
# "emergency=15" sets up the digital port 15 as emergency stop, when pressed the
# program will be terminated. Remove it if you want to utilize the sensor port 15.
with connect(emergency=15) as hedgehog:
    # Write your code here
    # E.g. simply output text to the console.
    print("Hello World")


##################################################
# Quick reference of the Hedgehog Python Library #
##################################################

# Motors and Servos
####################

# Move the motor at port 0 (port range from 0 to 3) at a given power
# (from -1000 fully backward to 1000 fully forward, 0 stops the motor).
# hedgehog.move(0, 1000)

# Set the servo at port 0 (port range from 0 to 3) to a given position
# (range from 0 to 2047).
# hedgehog.set_servo(0, 1024)

# Sensors
##########

# Read the value of the analog sensor at port 0 (port range from 0 to 7).
# Returned values are 12 bit integers (from 0 to 4095).
# hedgehog.get_analog(0)

# Read the value of the digital sensor at port 0 (port range from 8 to 15).
# Returnes a boolean value (True or False).
# hedgehog.get_digital(0)

# Enable the pullup resistor for the sensor at port 0 (port range from 0 to 15)
# The second parameter indicates whether the pullup resistor should be
# enabled (True) or diabled (False).
# hedgehog.set_input_state(0, True)

# iRobot Create
#########

# Just like with the Hedgehog Controller, a connection to the iRobot Create must
# be established, before you can use it.
# with connect_create() as create:
#     create.safe()
#     # Write your code here

# Drive the Create forward at 500 mm/s.
# The paramteters indicate the velocity of the left and right wheel in mm/s and
# range from -500 (fully backward) to 500 (fully forward).
# create.drive_direct(500, 500)

# Utility Functions
####################

# Pause the program execution for a 2 seconds.
# The Argument indicates how long the program should be paused.
# The number can also be a floating point value (e.g. 0.5 for half a second)
# sleep(2.0)
