
GCC=gcc

all: steady-hands

steady-hands: steady-hands.o
	$(GCC) -lpigpio -lpthread steady-hands.o -o steady-hands

steady-hands.o: steady-hands.c
	$(GCC) -g -c steady-hands.c -o steady-hands.o

clean: clear

clear: 
	rm -rf *.o steady-hands obj bin *.depend *.layout 
