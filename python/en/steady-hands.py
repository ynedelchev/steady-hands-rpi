
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
import RPi.GPIO as GPIO
import time

startPin      = 14
endPin        = 23
wirePin       = 18
secPunishment = 0.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(startPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(endPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(wirePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Hi Dear Students")

while True:
        print("Please touch the startPin with the ring.")
        while not GPIO.input(startPin):
                time.sleep(0.8)

        print("Touch the endPin with the ring without touching the bent wire. ")
        numFailures = 0
        startTime = time.clock()

        while not GPIO.input(endPin):
                if GPIO.input(wirePin):
                        numFailures = numFailures + 1
                        print("Failures: "+ str(numFailures))
                        time.sleep(secPunishment)
        score = time.clock() - startTime + (numFailures * secPunishment)
        print("Spent time "+ str(score)+ " seconds. "+ str(numFailures) + " failure points.")
        
