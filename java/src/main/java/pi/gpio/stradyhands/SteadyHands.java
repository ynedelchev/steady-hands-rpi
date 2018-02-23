package pi.gpio.steadyhands;

import com.pi4j.io.gpio.Pin;
import com.pi4j.io.gpio.PinMode;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.GpioPinDigitalOutput;

/**
 * Схема на крачетата: https://www.raspberrypi.org/documentation/usage/gpio/images/a-and-b-physical-pin-numbers.png
 * Забележка: Крачета 3 и 5 винаги отчитат напрежение (1), когато се използват като входни (IN).
 * 
 * Write a description of class SteadyHands here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class SteadyHands
{
   public static void main(String[] args) throws Exception {

     Pin  startPin = RaspiPin.GPIO_08;
     Pin  endPin   = RaspiPin.GPIO_10;
     Pin  wirePin  = RaspiPin.GPIO_12;
     GpioPinDigitalInput start = null;
     GpioPinDigitalInput end   = null;
     GpioPinDigitalInput wire  = null;
     long punishmentMillis = 200;
     int  numFailures = 0;
   
     // get a handle to the GPIO controller
     final GpioController gpio = GpioFactory.getInstance();

   
     start = gpio.provisionDigitalInputPin(startPin, PinPullResistance.PULL_DOWN);
     end   = gpio.provisionDigitalInputPin(endPin,   PinPullResistance.PULL_DOWN);
     wire  = gpio.provisionDigitalInputPin(wirePin,  PinPullResistance.PULL_DOWN);

     gpio.setMode(PinMode.DIGITAL_INPUT, start);
     gpio.setMode(PinMode.DIGITAL_INPUT, end);
     gpio.setMode(PinMode.DIGITAL_INPUT, wire);

     System.out.println("Здравейте, мили ученици!");

       while (true) {
         System.out.println("Докоснете точка „Начало“");
         while (start.isLow()) {
           Thread.sleep(800);
         }

         System.out.println("А сега докоснете точка „Край“, без да докосвате жицата");
         numFailures = 0;
         long startTime = System.currentTimeMillis();

         while (! end.isLow()) {
                if (wire.isHigh()) {
                  numFailures = numFailures + 1;
                  System.out.println("Наказателни точки" + numFailures);
                  Thread.sleep(punishmentMillis);
                }
	 }
         long score = System.currentTimeMillis() - startTime + (numFailures * punishmentMillis);
         score = score / 1000;
         System.out.println("Изминало време " + score + " секунди. " + numFailures + " наказателни точки");
        
      }
      // release the GPIO controller resources
      //gpio.shutdown();
   }
}
