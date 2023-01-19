import RPi.GPIO as GPIO
import time

# Set the pin number for the power relay
relay_pin = 18

# Set the duration for the egg roller to be on (in seconds)
on_duration = 2

# Set the interval for the egg roller to turn on (in seconds)
interval = 10

# Set up the GPIO pin for output
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

while True:
    # Turn on the power relay (and egg roller)
    GPIO.output(relay_pin, GPIO.HIGH)
    # Wait for the on duration
    time.sleep(on_duration)
    # Turn off the power relay (and egg roller)
    GPIO.output(relay_pin, GPIO.LOW)
    # Wait for the interval before turning on again
    time.sleep(interval)