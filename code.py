import alarm
import time
import board
import digitalio

led= digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
#print("Waking up")

while True:

    # blink
    for i in range(0,10):
        led.value=True
        time.sleep(1)
        led.value=False
        time.sleep(1)

    # Set an alarm for 60 seconds from now.
    time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)

    # Deep sleep until the alarm goes off. Then restart the program.
    alarm.exit_and_deep_sleep_until_alarms(time_alarm)

    