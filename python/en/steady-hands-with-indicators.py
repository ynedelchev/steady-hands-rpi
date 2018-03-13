# python3
# Steady Hands Game

import RPi.GPIO as GPIO
import time
from gpiozero import LED    # sudo apt install python3-gpiozero

# Note: Pin 3 (GPIO2) and 5 (GPIO3) always detect 1 (True), when are used as input (IN) and nothing touches them.
startPin = 14       # BOARD: 8 = BCM: 14
endPin = 15         # BOARD: 10 = BCM: 15
wirePin = 18        # BOARD: 12 = BCM: 18
greenLED = LED(17)  # BOARD: 11 = BCM: 17
redLED = LED(27)    # BOARD: 13 = BCM: 27
buzzer = 22         # BOARD: 15 = BCM: 22
secondsToPauseOnFailure = 0.2

def beep(seconds = 0.05):
    GPIO.output(buzzer, True)
    time.sleep(seconds)
    GPIO.output(buzzer, False)

def showFailure(seconds):
    greenLED.off()
    redLED.on()
    GPIO.output(buzzer, True)
    time.sleep(seconds)
    redLED.off()
    greenLED.on()
    GPIO.output(buzzer, False)

# Pin enumeration http://raspi.tv/wp-content/uploads/2014/07/Raspberry-Pi-GPIO-pinouts.png
GPIO.setmode(GPIO.BCM)
GPIO.setup(startPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(endPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(wirePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer, GPIO.OUT)

print("Hello!")

while True:
        print("Touch Start")
        while not GPIO.input(startPin):
                time.sleep(0.01)

        beep()
        greenLED.on()
        print("Now touch End, without touching the wire")
        numberOfFailures = 0
        startTime = time.clock()

        while not GPIO.input(endPin):
                if GPIO.input(wirePin):
                        numberOfFailures = numberOfFailures + 1
                        print("Failures", numberOfFailures)
                        showFailure(secondsToPauseOnFailure)

        score = time.clock() - startTime + (numberOfFailures * secondsToPauseOnFailure)
        print("Time", score, "seconds.", numberOfFailures, " failures")
        beep()
        greenLED.off()
GPIO.cleanup()
