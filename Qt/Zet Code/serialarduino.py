import serial # if you have not already done so
import time
ser = serial.Serial('/dev/tty.usbmodem1411', 9600) #Mac OS X
#ser = serial.Serial('/dev/ttyACM0', 9600) #Raspberry Pi
time.sleep(2)
ser.write("on")
print "Sent"


################
#			   #
# ARDUINO CODE #
#			   #
################
#
#
# /*
#  Simple LED sketch
#  */
     
# int led = 13; // Pin 13
     
# void setup()
# {
#     pinMode(led, OUTPUT); // Set pin 13 as digital out
     
#     // Start up serial connection
#     Serial.begin(9600); // baud rate
#     Serial.flush();
# }
     
# void loop()
# {
#     String input = "";
     
#     // Read any serial input
#     while (Serial.available() > 0)
#     {
#         input += (char) Serial.read(); // Read in one char at a time
#         delay(5); // Delay for 5 ms so the next char has time to be received
#     }
     
#     if (input == "on")
#     {
#         if (digitalRead(13) == HIGH)
#         {
#           Serial.write("Led is already ON \n");
#         }
#         else
#         {
#           digitalWrite(led, HIGH); // on
#           Serial.write("LED is on \n");
#         }
#     }
#     else if (input == "off")
#     {
#         if (digitalRead(13) == LOW)
#         {
#           Serial.write("Led is already OFF \n");
#         }
#         else
#         {
#           digitalWrite(led, LOW); // on
#           Serial.write("LED is off \n");
#         }
#     }
# }
