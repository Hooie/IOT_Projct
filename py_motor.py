#py_motor.py

import RPi.GPIO as GPIO
import time

servo_pin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0.0)
time.sleep(1)

def TurnOn():
	pwm.ChangeDutyCycle(9.5)
	time.sleep(1.0)

def TurnOff():
	pwm.ChangeDutyCycle(6.0)
	time.sleep(1.0)
	
def Stop():
	pwm.stop()
	GPIO.cleanup()
	
#모터의 적정 duty값 체크
def Checkmotor():
	i = 1
	while i:
		val = 0.1 + (i/10)
		pwm.ChangeDutyCycle(val)
		print(val)
		i += 1
		time.sleep(1.5)
