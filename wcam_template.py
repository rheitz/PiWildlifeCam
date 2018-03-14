# Ryan Heitz and BT
# March 14, 2018
# Wildlife camera project

# Imports and variables needed
import time
import RPi.GPIO as GPIO
from picamera import PiCamera

button_pin = 21 # this is where the wires are plugged into the Pi
PIR_pin = 17
LED_pin = 20
camera_on = False # flag is down until the button is pressed
frame = 1
# Functions go here


# Setup for GPIO (button, LED, PIR,IR LEDs (later))
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(PIR_pin, GPIO.IN)
GPIO.setup(LED_pin, GPIO.OUT)

# Setup Camera
camera = PiCamera()

# Main Program
# Loop forever
while True:
    # Toggle on and off the motion-sensing loop using button
    if GPIO.input(button_pin):
        # Flip the flag (True --> False; False --> True)
        if camera_on == True:
            camera_on = False
        else:
            camera_on = True
    
    # Check for motion, if motion detected
    if camera_on == True and GPIO.input(PIR_pin):
        try:
            # create the filename (should increment, so each is unique)
            # Take picture or video
            camera.capture('/home/pi/wcam/frame%03d.jpg' % frame)
            frame += 1
        except:
            print("Oops, I couldn't take the picture. :<")

    if camera_on == True:
        GPIO.output(LED_pin,GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(LED_pin,GPIO.LOW)
    # Pause for a second  
    time.sleep(1)
# Loop around
