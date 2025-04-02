"""
Examples of how to use RPIO as a drop-in replacement for RPi.GPIO
RPIO Documentation: http://pythonhosted.org/RPIO
"""
import RPi.GPIO as GPIO
import time

# set up GPIO output channel
GPIO.setup(21, GPIO.OUT)

while(1):
# flash led on GPIO 21
  GPIO.output(21, GPIO.HIGH)  
  time.sleep(1)
  GPIO.output(21, GPIO.LOW)
  time.sleep(1)

