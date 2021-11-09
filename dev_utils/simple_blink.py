import board
import digitalio
import time
from microcontroller import watchdog as w
from watchdog import WatchDogMode
led= digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
#w.timeout=4 # Set a timeout of 2.5 seconds
#w.mode = WatchDogMode.RESET

while True:
    led.value=True
    time.sleep(1)
    led.value=False
    time.sleep(1)
