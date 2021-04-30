# -------------------------------------------------
# Servo Example
# -------------------------------------------------
# 3.3v = 1,17, 5.0v =2,4 GND = 6,9,14,20,25,30,34,39
# I/O = 3,5,7,8,10,11,12,13,15,16,18,19,21,22,23,24,
# More I/O =26,27,28,29,31,32,33,35,36,37,38,40
# -------------------------------------------------
#
import RPi.GPIO as GPIO
import time

servoPin = 11 # Physical pin 11 and BCM pin GPIO17
GPIO.setmode(GPIO.BOARD) # Note: physical pins on the Raspberry Pi Header 
GPIO.setwarnings(False)
GPIO.setup(servoPin, GPIO.OUT)

pwm = GPIO.PWM(servoPin, 50) # GPIO 17 for PWM with 50Hz
pwm.start(0) # Initialization - set to 0 deg

def set_angle(angle,io_pin):
    percent = 18
    duty = (angle/percent) + 2
    maxSleep = .5 # max time needed to move from 0 to 180
    GPIO.output(io_pin, True)
    servoUT.ChangeDutyCycle(duty)
    print('Angle:',angle, 'DutyCycle:',duty)
    time.sleep(maxSleep)
    GPIO.output(io_pin, False)
    servoUT.ChangeDutyCycle(0)



set_angle(angle0,servoPin)
time.sleep(2)
set_angle(angle90,servoPin)
time.sleep(2)
set_angle(angle0,servoPin)
time.sleep(2)
set_angle(angle180,servoPin)
time.sleep(2)
set_angle(angle0,servoPin)
time.sleep(2)
set_angle(angle90,servoPin)
time.sleep(2)
set_angle(angle0,servoPin)
time.sleep(2)
set_angle(angle180,servoPin)
time.sleep(2)
set_angle(angle0,servoPin)
time.sleep(2)
    
GPIO.cleanup()  
print('Done')
