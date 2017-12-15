# python3
# Steady hands game

import RPi.GPIO as GPIO
import time

# use BCM GPIO numbering. Do not use anything else.
GPIO.setmode(GPIO.BCM)

i = 0
while i < 20:
        GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        i = i + 1


# set up GPIO input pins
# (pull_up_down be PUD_OFF, PUD_UP or PUD_DOWN, default PUD_OFF)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO 0 & 1 have hardware pull ups fitted in the Pi so don't enable them
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

print("Hi from Python :- SteadyHands game")
delay = range(0,5000)
dum = 0
start_rest = 4
end_rest = 2
wire = 3
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
	#while True:
		#time.sleep(0.2)
		if GPIO.input(wire) == 0:
			penalty = penalty + 1
			print("Penalties total", penalty, " points")
			time.sleep(0.07)
		strr = " "
		i = 0
		while i < 20:
			if GPIO.input(i) != 0:
				strr = strr + str(i) + "  "
			i = i + 1
		#print (strr)
	score = time.clock() - run_time + (penalty * 0.07)
	print("The run time was", score, "seconds with", penalty, "Penalty points")
#finished a run so start again
