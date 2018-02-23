#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <pigpio.h>

/* 
 * Моля изпълнете: 
 *     sudo apt-get install codeblocks vim gcc pigpio make
 * След това компилирайте със 
 *     make
 * и ще получите изпълним файл `steady-hands`
 * или просто стартирайте развойната среда Code Blocks и отворете проектния файл `steady-hands.cbp`.
 *
 * Схема на крачетата: https://www.raspberrypi.org/documentation/usage/gpio/images/a-and-b-physical-pin-numbers.png
 * Забележка: Крачета 3 и 5 винаги отчитат напрежение (1), когато се използват като входни (IN).
 */
int main(int argc, char* argv[])//           startPin endPin  wirePin
{                               //                  |    |    |
  int  startPin       =  8;     //   +--------------V----V----V--------------------------------------... . . 
  int  endPin         = 10;     //   | (2) (4) (6) (8) (10) (12) (14) (16) (18) (20) (22) (24) (26)
  int  wirePin        = 12;     //   | (1) (3) (5) (7) ( 9) (11) (13) (15) (17) (19) (21) (23) (25)
  int  secsPunishment =  1;     //   |
  int  numFailures    =  0;     //   |    R a s p b e r r y   P i   b o a r d
  long startTime      =  0;     //   .
  int  score          =  0;     //   . . .  .  .  .   .   .   .    .    .    .     .     .     .
  

  if (gpioInitialise() < 0) {
    printf("\nError initializing GPIO. Please make sure you are executing it with sudo.\n\n");
    return 1;
  }

  gpioSetMode(17, PI_INPUT); 

  gpioSetMode(startPin, PI_INPUT);
  gpioSetMode(endPin,   PI_INPUT);
  gpioSetMode(wirePin,  PI_INPUT);

  printf("Здравейте, мили ученици!\n");

  while (1) {
    printf("Докоснете точка „Начало“\n");
    while ( ! gpioRead(startPin) ) {
      sleep(1); // Sleep for one second.
    }
    printf("А сега докоснете точка „Край“, без да докосвате жицата\n");
    numFailures = 0;
    startTime = clock();
    score = 0;
    while ( ! gpioRead(endPin)) {
      if (gpioRead(wirePin)) {
        numFailures = numFailures + 1;
        printf("Наказателни точки %d\n", numFailures);
        sleep(secsPunishment);
      }
    }
    score = clock() - startTime + (numFailures * secsPunishment);
    printf("Изминало време %d секунди. %d наказателни точки\n", score, numFailures);
  }
  gpioTerminate();
  return 0;
}

