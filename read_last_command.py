# Raspberry Pi Robot Project
import requests
import RPi.GPIO as GPIO
import time

LED1 = 3
LED2 = 5
LED3 = 7
RED = 8
GRN = 10
BLU = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)

GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GRN,GPIO.OUT)
GPIO.setup(BLU,GPIO.OUT)

# Challenge 5
my_robot_name = 'robot2'

def robotDeviceSetup():
    # set robot devices into a default startup state
    robotLEDReset()
    robotRGBReset()
    
def robotLEDReset():
    # set robot devices into a default startup state
    GPIO.output(LED1,0)
    GPIO.output(LED2,0)
    GPIO.output(LED3,0)

def robotRGBReset():
    # set robot devices into a default startup state
    GPIO.output(RED,0)
    GPIO.output(GRN,0)
    GPIO.output(BLU,0)

# Challenge 6
def robotLED(device, action) :
    print('LED on/off Function')
    print('The robot device is',device,'the robot action is',action,)
    if device == 'led-1':
        if action == 'on':
            print('turn on LED 1')
            GPIO.output(LED1,GPIO.HIGH)
            #this is where you turn on the GPIO
        elif action == 'off':
            print('turn off LED 1')
            GPIO.output(LED1,GPIO.LOW)
            #this is where you turn on the GPIO
        else :
            print('warning: LED 1 Action - should not see this message')
    elif device == 'led-2':
        if action == 'on':
            print('turn on LED 2')
            GPIO.output(LED2,1)
            #this is where you turn on the GPIO
        elif action == 'off':
            print('turn off LED 2')
            GPIO.output(LED2,0)
            #this is where you turn on the GPIO
        else :
            print('warning: LED 2 Action - should not see this message')
    elif device == 'led-3':
        if action == 'on':
            print('turn on LED 3')
            GPIO.output(LED3,1)
            #this is where you turn on the GPIO
        elif action == 'off':
            print('turn off LED 3')
            GPIO.output(LED3,0)
            #this is where you turn on the GPIO
        else :
            print('warning: LED 3 Action - should not see this message')
    else :
        print('warning: LED Function Flow Error - should not see this message')
        
def robotRGB(device, action) :
    print('RGB LED Function')
    print('The robot device is',device,'the robot action is',action,)
    
    if action == 'red':
        robotRGBReset()
        print('turn RGB LED Red')
        GPIO.output(RED,1)        
        #this is where you send the Red code to the RGB LED GPIO
        time.sleep(2)
    elif action == 'green':
        robotRGBReset()
        print('turn RGB LED Green')
        GPIO.output(GRN,1)
        #this is where you send the Green code to the RGB LED GPIO
        time.sleep(2)
    elif action == 'blue':
        robotRGBReset()
        print('turn RGB LED Blue')
        GPIO.output(BLU,1)
        #this is where you send the Blue code to the RGB LED GPIO
        time.sleep(2)
    elif action == 'off':
        print('turn RGB LED OFF')
        robotRGBReset()
        #this is where you send the Green code to the RGB LED GPIO
        time.sleep(2)
    else :
        print('warning: RGB LED Function Non Screened Color',action)
        
def robotServo(device, action) :
    print('Servo Function')
    print('The robot device is',device,'the robot action is',action,)
    
    if action == 'wave':
        print('send servo wave')
        #this is where you send the wave pattern to the servo
    elif action == '0':
        print('turn servo to 0')
        #this is where you send the position 0 to the servo
    elif action == '90':
        print('turn servo to 90')
        #this is where you send the position 90 to the servo
    elif action == '180':
        print('turn servo to 180')
        #this is where you send the position 180 to the servo
    else :
        print('warning: Servo Function Non Screened position',action) 



#remote_robot_file_name = input('enter Robot name > ')
robotDeviceSetup()
remote_robot_file_name = 'all_robots_command_requests'
file_name = remote_robot_file_name + '.txt'
url = 'https://www.steamclown.org/projects/QInlIj_vIHev/Huch_QIn/' + file_name
print(url)

while (True):
    
    r = requests.get(url)
    whole_file = r.text
    print(whole_file)

    # This splits the big string of whole_file into
    # a list of lines, where each item in the list
    # is a single line as a string
    lines = whole_file.split()
    # This gets the lines and finds the last line
    # and splits the line into a new list of robot_data
    line_count = (len(lines))
    line = lines[line_count-1]  # this is the length -1 because the index starts at 0 not 1
    robot_data = line.split(',')
    # This loops through the list of lines, and splits
    # each line into a new list of robot_data
    # This take the first index object in the
    # list robot_data.  This is the robot_name
    robot_name = robot_data[0]
        
    # This if let's you ask if the robot_name
    # is your robot. If it is, then you can do stuff
    if robot_name == my_robot_name:
        print('---------------------------')
        print('This Command is for me, My name is',robot_name)
        print(robot_data)
        robot_device = robot_data[1]
        robot_action = robot_data[2]
        robot_date = robot_data[3]
        robot_time = robot_data[4]
        print('Robot Name is ',robot_name)
        print('Robot Device is ',robot_device)
        print('Robot Action is ',robot_action)
        print('Robot Date is ',robot_date)
        print('Robot Time is ',robot_time)
        print('---------------------------')
        if robot_device == 'led-1' or robot_device == 'led-2' or robot_device == 'led-3':
            robotLED(robot_device, robot_action)
        elif robot_device == 'rgb-led' :
            robotRGB(robot_device, robot_action)
        elif robot_device == 'servo' :
            robotServo(robot_device, robot_action)
        print('---------------------------')
        
        time.sleep(10)
print('Done')
