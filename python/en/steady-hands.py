
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
#                  A         C         B
#                  |         |         |
#   /==============V=========V=========V=================== = =  =   ~
#   | 5V  5V  GR  14   15   18   -    23   24   -    25    8
#   | (2) (4) (6) (8) (10) (12) (14) (16) (18) (20) (22) (24) . . .          
#   | (1) (3) (5) (7) ( 9) (11) (13) (15) (17) (19) (21) (23) . . .  ~
#   | 3V   2   3   4   -    17   27   22   -^   10    9   11 
#   |                                       |
#   |                                       |                        ~ 
#    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~|~ ~ ~ ~ ~ ~ ~ ~  ~  ~   ~
#                                           |
#                                           D
#
# See Also: 
#   https://github.com/trayanmomkov/Raspberry-Pi/blob/master/Python/steady-hands-max-failures.py
#   https://github.com/trayanmomkov/Raspberry-Pi/blob/master/Python/steady-hands-start-reset.py
#   https://github.com/trayanmomkov/Raspberry-Pi/blob/master/Python/steady-hands-with-indicators.py
#   https://github.com/trayanmomkov/Raspberry-Pi/blob/master/Python/%D1%81%D1%82%D0%B0%D0%B1%D0%B8%D0%BB%D0%BD%D0%B8_%D1%80%D1%8A%D1%86%D0%B5_%D1%81_%D0%B8%D0%BD%D0%B4%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D1%80%D0%B8.py
import RPi.GPIO as GPIO
import time

# Pins
startPin      = 14      # BCM GPIO14 = BOARD pin 8
endPin        = 23      # BCM GPIO23 = BOARD pin 16
wirePin       = 18      # BCM GPIO18 = BOARD pin 12

secondsPunishment = 0.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(startPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(endPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(wirePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Hi Dear Students")

while True:
        print("Please touch the startPin with the ring.")
        while not GPIO.input(startPin):
                time.sleep(0.01)

        print("Touch the endPin with the ring without touching the bend wire. ")
        numberOfFailures = 0
        startTime = time.clock()

        while not GPIO.input(endPin):
                if GPIO.input(wirePin):
                        numberOfFailures = numberOfFailures + 1
                        print("Failures: "+ str(numberOfFailures))
                        time.sleep(secondsPunishment)
        score = time.clock() - startTime + (numberOfFailures * secondsPunishment)
        print("Spent time "+ str(score)+ " seconds. "+ str(numberOfFailures) + " failure points.")
        
