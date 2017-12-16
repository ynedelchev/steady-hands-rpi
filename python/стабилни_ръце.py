# python3
# Играта „Стабилни ръце“

import RPi.GPIO as GPIO
import time

# Схема на крачетата: https://www.raspberrypi.org/documentation/usage/gpio/images/a-and-b-physical-pin-numbers.png
# Забележка: Крачета 3 и 5 винаги отчитат напрежение (1), когато се използват като входни (IN).
началноКраче = 8
крайноКраче = 10
крачеЖица = 12
секундиПаузаПриНаказание = 0.2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(началноКраче, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(крайноКраче, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(крачеЖица, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Здравейте, мили ученици!")

while True:
        print("Докоснете точка „Начало“")
        while not GPIO.input(началноКраче):
                time.sleep(0.8)

        print("А сега докоснете точка „Край“, без да докосвате жицата")
        наказателниТочки = 0
        началноВреме = time.clock()

        while not GPIO.input(крайноКраче):
                if GPIO.input(крачеЖица):
                        наказателниТочки = наказателниТочки + 1
                        print("Наказателни точки", наказателниТочки)
                        time.sleep(секундиПаузаПриНаказание)
        score = time.clock() - началноВреме + (наказателниТочки * секундиПаузаПриНаказание)
        print("Изминало време", score, "секунди.", наказателниТочки, " наказателни точки")
        
