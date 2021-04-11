# Loop forever spinning the PWM up and down
# Written by Glen Darling, April 2021

import Jetson.GPIO as GPIO
import time

# When VERBOSE is True a line of text is printed each change in duty cycle
VERBOSE = False

# Setup the PWM GPIO
GPIO.setmode(GPIO.TEGRA_SOC)
GPIO.setup('LCD_BL_PW', GPIO.OUT)
pwm = GPIO.PWM('LCD_BL_PW', 100)
pwm.start(0)

while True:
  for dc in range(5, 40, 5):
    if VERBOSE: print(dc)
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.1)
  for dc in range(35, 0, -5):
    if VERBOSE: print(dc)
    pwm.ChangeDutyCycle(dc)
    time.sleep(0.1)

