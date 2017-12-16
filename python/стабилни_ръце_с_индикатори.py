# python3
# Играта „Стабилни ръце“

import RPi.GPIO as GPIO
import time
from gpiozero import LED    # sudo apt install python3-gpiozero

# Забележка: Крачета 3 и 5 винаги отчитат напрежение (1), когато се използват като входни (IN).
началноКраче = 14 # BOARD: 8 = BCM: 14
крайноКраче = 15 # BOARD: 10 = BCM: 15
крачеЖица = 18 # BOARD: 12 = BCM: 18
зеленСветодиод = LED(17) # BOARD: 11 = BCM: 17
червенСветодиод = LED(27) # BOARD: 13 = BCM: 27
сирена = 22 # BOARD: 15 = BCM: 22
секундиПаузаПриНаказание = 0.2

# Схема на крачетата http://raspi.tv/wp-content/uploads/2014/07/Raspberry-Pi-GPIO-pinouts.png
GPIO.setmode(GPIO.BCM)
GPIO.setup(началноКраче, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(крайноКраче, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(крачеЖица, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(сирена, GPIO.OUT)

print("Здравейте, мили ученици!")

while True:
        print("Докоснете точка „Начало“")
        while not GPIO.input(началноКраче):
                time.sleep(0.8)

        зеленСветодиод.on()
        print("А сега докоснете точка „Край“, без да докосвате жицата")
        наказателниТочки = 0
        началноВреме = time.clock()

        while not GPIO.input(крайноКраче):
                if GPIO.input(крачеЖица):
                        наказателниТочки = наказателниТочки + 1
                        print("Наказателни точки", наказателниТочки)
                        зеленСветодиод.off()
                        червенСветодиод.on()
                        GPIO.output(сирена, True)
                        time.sleep(секундиПаузаПриНаказание)
                        червенСветодиод.off()
                        зеленСветодиод.on()
                        GPIO.output(сирена, False)
        score = time.clock() - началноВреме + (наказателниТочки * секундиПаузаПриНаказание)
        print("Изминало време", score, "секунди.", наказателниТочки, " наказателни точки")
        зеленСветодиод.off()
GPIO.cleanup()

