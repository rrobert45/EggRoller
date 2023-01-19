import RPi.GPIO as GPIO
import time
import csv
from datetime import datetime

# Set the pin number for the power relay
relay_pin = 17

# Set the duration for the egg roller to be on (in seconds)
on_duration = 120

# Set the interval for the egg roller to turn on (in seconds)
interval = 14280

# Set up the GPIO pin for output
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Open a CSV file for logging
with open('egg_roller_log.csv', mode='a') as log_file:
    log_writer = csv.writer(log_file)
    if log_file.tell() == 0:
        log_writer.writerow(["Date", "Time", "Event"])
    try:
        while True:
            # Turn on the power relay (and egg roller)
            GPIO.output(relay_pin, GPIO.HIGH)
            print("ON")
            current_time = datetime.now()
            log_writer.writerow([current_time.strftime("%m/%d/%Y"), current_time.strftime("%H:%M:%S"), "Relay Turned ON"])
            # Wait for the on duration
            time.sleep(on_duration)
            # Turn off the power relay (and egg roller)
            GPIO.output(relay_pin, GPIO.LOW)
            print("OFF")
            current_time = datetime.now()
            log_writer.writerow([current_time.strftime("%m/%d/%Y"), current_time.strftime("%H:%M:%S"), "Relay Turned OFF"])
            # Wait for the interval before turning on again
            time.sleep(interval)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()