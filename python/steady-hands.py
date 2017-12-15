# python3
# Steady hands game
#  Do a hardware setup with wires like this: 
#                    __
#           _______ /__\______
#          /        \__/      \
#         /            \       \
#        /              \       \
#  -+    |               |       |    +-
# ==|====|============== | ======|====|======== stable base
#   A    C               D            B  
# start  wire            dum          end
# rest                                rest
#
# Where D is a wire loop around the wire C.
# Connect them to the pins in the RaspberryPi board like this:
#
#              D
#              |
#   /==========|=========================================== = =  =   ~
#   | ( ) ( ) (v) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) . . .          
#   | ( ) (o) (o) (o) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) . . .          ~
#   |      ^   ^   ^                                                 
#   |      |   |   |                                                 ~ 
#    ~ ~ ~ | ~ | ~ | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  ~  ~   ~
#          |   |   |
#          B   C   A
#

import RPi.GPIO as GPIO
import time

# use BCM GPIO numbering. Do not use anything else.
GPIO.setmode(GPIO.BCM)

dum = 0
start_rest = 4
end_rest = 2
wire = 3

# set up GPIO input pins
# (pull_up_down be PUD_OFF, PUD_UP or PUD_DOWN, default PUD_OFF)
GPIO.setup(start_rest, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(end_rest, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(wire, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

# GPIO 0 & 1 have hardware pull ups fitted in the Pi so don't enable them
GPIO.setup(dum, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

print("Hi from Python :- SteadyHands game")
delay = range(0,5000)
while True:
#wait until the wand is at the start
	print("Move the loop to the start rest")
	while GPIO.input(start_rest) != 0:
		time.sleep(0.8)
	
	#now we are at the start of the bendy wire
	print("Start when you are ready")
	#wait until the loop is lifted off the wire
	while GPIO.input(start_rest) == 0:
		time.sleep(0.1)
	print("You're off")
	#time the run to the other rest
	penalty = 0
	run_time = time.clock()
	
	while GPIO.input(end_rest) != 0:
		if GPIO.input(wire) == 0:
			penalty = penalty + 1
			print("Penalties total", penalty, " points")
			time.sleep(0.07)
	score = time.clock() - run_time + (penalty * 0.07)
	print("The run time was", score, "seconds with", penalty, "Penalty points")
#finished a run so start again
