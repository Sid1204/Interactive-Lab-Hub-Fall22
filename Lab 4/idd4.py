import qwiic
import time
import time
from adafruit_servokit import ServoKit
import os
from playsound import playsound

kit = ServoKit(channels=16)
servo = kit.servo[1]
servo.set_pulse_width_range(500, 2500)

ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
    print("Sensor online!\n")
	
while True:
    try:
        ToF.start_ranging()						 # Write configuration bytes to initiate measurement
        time.sleep(.005)
        distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
        time.sleep(.005)
        ToF.stop_ranging()

        distanceInches = distance / 25.4
        distanceFeet = distanceInches / 12.0

        if distance<=1000 and distance>=975:
            playsound('//home//pi//Interactive-Lab-Hub-Fall22//Lab 4//IDD4-1.mp3', True)
            time.sleep(3)
            
        if distance<=325 and distance>=300:
            playsound('//home//pi//Interactive-Lab-Hub-Fall22//Lab 4//IDD4-2.mp3', True)
            time.sleep(3)
            
        if distance<=125:
            try:
                os.system("python /home/pi/Interactive-Lab-Hub-Fall22/Lab\ 2/image.py")
                servo.angle = 90
                time.sleep(8)
            except KeyboardInterrupt:
                servo.angle = 0
                time.sleep(0.5)
                break
            
    except Exception as e:
        print(e)