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

GPIO.setmode(GPIO.BOARD) # Note: physical pins on the Raspberry Pi Header 
GPIO.setwarnings(False)

servoPIN = 11 # Physical pin 11 and BCM pin GPIO17
GPIO.setup(servoPIN, GPIO.OUT)

robot_servo = GPIO.PWM(servoPIN, 50) # Set PWM with 50Hz
# test PWM min and max range. Typical is 0,7,10,
# but all servos are a little diffrent.  Experement limits
# to set the 0 to 90 to 180 values. Eyeball it...
pos180 = 11.5
pos90 = 6.5
pos0 = 2.5

robot_servo.start(pos90) # Initialization Start Position
time.sleep(1)
try:
  while True:
      for i in range(5):
          robot_servo.ChangeDutyCycle(pos0)
          print('pwm degrees = 0')
          time.sleep(1)
          robot_servo.ChangeDutyCycle(pos90)
          print('pwm degrees = 90')
          time.sleep(1)
          robot_servo.ChangeDutyCycle(pos180)
          print('pwm degrees = 180')
          time.sleep(1)
      for i in range(2,12):
          robot_servo.ChangeDutyCycle(i)
          print('pwm degrees = ', i)
          time.sleep(.2)
      for i in range(12,2,-1):
          robot_servo.ChangeDutyCycle(i)
          print('pwm degrees = ', i)
          time.sleep(.2)
          
          
except KeyboardInterrupt:
  robot_servo.stop()

GPIO.cleanup()  
print('Done')
