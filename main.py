"""
Examples of how to use RPIO as a drop-in replacement for RPi.GPIO
RPIO Documentation: http://pythonhosted.org/RPIO
"""
import RPIO
import time

# set up GPIO output channel
RPIO.setup(8, RPIO.OUT)

while(1):
# flash led on GPIO 21
  RPIO.output(21, True)
  time.sleep(1)
  RPIO.output(8, False)
  time.sleep(1)


# reset every channel that has been set up by this program,
# and unexport interrupt gpio interfaces
RPIO.cleanup()
