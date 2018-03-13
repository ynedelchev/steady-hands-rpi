/**
    wget http://get.pi4j.com/download/pi4j-1.2-SNAPSHOT.deb
    dpkg -i pi4j-1.2-SNAPSHOT.deb
    javac -classpath .:classes:/opt/pi4j/lib/'*' -d . SteadyHands.java
    java -classpath .:classes:/opt/pi4j/lib/'*' SteadyHands
*/


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
 * Scheme: https://www.raspberrypi.org/documentation/usage/gpio/images/a-and-b-physical-pin-numbers.png
 */
public class SteadyHands {
   public static void main(String[] args) throws Exception {

     Pin  startPin = RaspiPin.GPIO_15;
     Pin  endPin   = RaspiPin.GPIO_16;
     Pin  wirePin  = RaspiPin.GPIO_01;
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

     System.out.println("Hi!");

       while (true) {
         System.out.println("Touch Start");
         while (start.isLow()) {
           Thread.sleep(800);
         }

         System.out.println("Touch End");
         numFailures = 0;
         long startTime = System.currentTimeMillis();

         while (! end.isLow()) {
                if (wire.isHigh()) {
                  numFailures = numFailures + 1;
                  System.out.println("Failures" + numFailures);
                  Thread.sleep(punishmentMillis);
                }
	 }
         long score = System.currentTimeMillis() - startTime + (numFailures * punishmentMillis);
         score = score / 1000;
         System.out.println("Time " + score + " seconds. " + numFailures + " failures");
        
      }
      // release the GPIO controller resources
      //gpio.shutdown();
   }
}
