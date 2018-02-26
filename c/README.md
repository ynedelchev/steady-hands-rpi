Steady Hands Game realized with Raspberry Pi in C
=================================================

This is a C implementation for the Steady Hands game for Raspberry Pi.

Prerequisites
-------------

Install the GPIO native library for Raspberry Pi.
````
  sudo apt-get install pigpio
````

Optionally install wiringpi toolset
````
  sudo apt-get install wiringpi
````

There are two numbering schemes for the pins of the Raspberry Pi - Physical and Broadcom numbering (BCM). 
The `pigpio` library uses just the *BCM* scheme. 
You can run the `gpio readall` to see how the schemes map to each other. 
Sample output:
````
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
````

So here, you can see that for example Physical pin 8 corresponds to BCM pin 14. 
Physical 12 corresponds to BCM 18 and Physical pin 16 corresponds to BCM pin 23. 
These are the pins that we would use in our program.

If you look at the Raspberry Pi, with the pins as two columns on the right side of the 
board, then the top left pin would be physical pin 1 and the top right pin will be physical pin 2.


The Game
--------

The game requires you to move a wire ring along a bent wire without touching them. 
To be able to mark the start and end of the game we have two additional start and end rest slots 
near the beginning and the end of the bent wire. 

Each of these elements (start slot, bent wire, end slot) are connected to Raspberry pins in input mode
and the wire ring is connected to a pin with 3.3V., so when the ring wire does not touch anything - all 
of the input pins will return 0. When it touches one of them, then it would return 1.

````
                      __
             _______ /__\______
            /        \__/      \
           /            \       \
          /              \       \
   -+    |               |       |    +-
  ==|====|============== | ======|====| ========  stаblе bаsе
    А    c               D            В  
 stаrt  wirе            dum          еnd
  rеst                               rest

````

In our program we are connecting 


|   | Name       | Physical Pin | Broadcom Pin (BCM) |
|---|------------|--------------|--------------------|
| A | Start Rest |       8      |         14         |
| B | End Rest   |      16      |         23         |
| C | Bent Wire  |      12      |         18         |
| D | Wire Ring  |      17      |         3.3V       |



Algorithm
---------

Тhе gаmе is in thrеее рhаsеs:

 1. Wаit untill thе lоор is рlасеd оn thе stаrt rеst.
 2. Wаit untill thе lоор is rеmоvеd frоm thе stаrt rеst.
 3. Тimе thе intеrvаl frоm lifting it оff thе stаrt rеst unti it rеасhеs thе еnd rеst. Whilе it is in this рhаsе thе Рi will mоnitоr thе bеndу wirе fоr tоuсhеs.

Тhis is thеn rереаtеd fоrеvеr, sо а соntrоl c is nееdеd tо stор thе рrоgrаm.

The `pigpio` library
--------------------

The `pigpio` library is documented here: [http://abyz.me.uk/rpi/pigpio](http://abyz.me.uk/rpi/pigpio/).
So you can see what is possible with it.


In our small program we are using just 

  * [gpioInitialise()](http://abyz.me.uk/rpi/pigpio/cif.html#gpioInitialise)
  * [gpioTerminate(void)](http://abyz.me.uk/rpi/pigpio/cif.html#gpioTerminate)
  * [gpioSetMode(unsigned gpio, unsigned mode)](http://abyz.me.uk/rpi/pigpio/cif.html#gpioSetMode)
  * [gpioRead(unsigned gpio)](http://abyz.me.uk/rpi/pigpio/cif.html#gpioRead)

Compile with makefile
---------------------

Just run 
````
  make 
````
and it will compile the program (`steady-hands.c`) and produce an executable file: `steady-hands`.

Compile with Code Blocks
------------------------

Install Code Blocks:
````
   sudo apt-get install codeblocks
````

Open the Code Blocks project `steady-hands.cbp` in Code Blocks and compile from there.

Run
---

You need to run it as `root`:
````
  sudo ./steady-hands
````


