import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import datetime
import cv2
import os


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline='#998877', fill='#FEE6E4')
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/piboto/Piboto-Bold.ttf", 24)
font3 = ImageFont.truetype("/usr/share/fonts/truetype/piboto/Piboto-Bold.ttf", 18)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()
val = 0

#def f(video):
    #os.environ['DISPLAY'] = display
    #print(os.environ['DISPLAY'])
    #a = cv2.imread('avatar.png')
    #cv2.imshow('window on %s'%display, a)
    
                #disp.image(frame, rotation)
    #cv2.waitKey(1000)
    #time.sleep(33)

def breathing():
    x = -(40 * padding)
    y = top - 24 * padding
    i = 1
    draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
    draw.text((x, y), "Inhale", font=font2, fill="#FF0000")
    disp.image(image, rotation)
    time.sleep(3)
    while i < 6:
        draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
        draw.text((x, y), str(i), font=font2, fill="#FF0000")
        disp.image(image, rotation)
        time.sleep(1)
        i+=1
    i = 1
    draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
    draw.text((x, y), "Hold", font=font2, fill="#FF0000")
    disp.image(image, rotation)
    time.sleep(3)
    while i < 6:
        draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
        draw.text((x, y), str(i), font=font2, fill="#FF0000")
        disp.image(image, rotation)
        time.sleep(1)
        i+=1
    i = 1
    draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
    draw.text((x, y), "Exhale", font=font2, fill="#FF0000")
    disp.image(image, rotation)
    time.sleep(3)
    while i < 6:
        draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
        draw.text((x, y), str(i), font=font2, fill="#FF0000")
        disp.image(image, rotation)
        time.sleep(1)
        i+=1
    i = 1
    draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
    draw.text((x, y), "Pause", font=font2, fill="#FF0000")
    disp.image(image, rotation)
    time.sleep(3)
    while i < 6:
        draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
        draw.text((x, y), str(i), font=font2, fill="#FF0000")
        disp.image(image, rotation)
        time.sleep(1)
        i+=1
        
        
    #image2 = Image.open("/home/pi/Interactive-Lab-Hub-Fall22/Lab 2/BB/BB1.jpeg")
    #image2 = image2.rotate(90)
    #image_ratio = image2.height / image2.width
    #height = disp.width
    #width = disp.height
    #screen_ratio = height / width
    #if screen_ratio < image_ratio:
    #    scaled_width = image2.width * height // image2.height
    #    scaled_height = height
    #else:
    #    scaled_width = width
    #    scaled_height = image2.height * width // image2.width
    #image2 = image2.resize((scaled_width, scaled_height), Image.BICUBIC)
    #print(image2.size)
    #a = scaled_width // 2 - width // 2
    #b = scaled_height // 2 - height // 2
    #image2 = image2.crop((a, b, a + width, b + height))
    #disp.image(image2)
    #time.sleep(1)


while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")

    #TODO: Lab 2 part D work should be filled in here. You should be able to look in cli_clock.py and stats.py 
    
    if buttonA.value and buttonB.value:
        y = top
        draw.text((x, y), "Press a button to \n", font=font, fill="#998877")
        y -= 8 * padding
        draw.text((x, y), "+1 Stress", font=font2, fill="#FF0000")
        y -= 16 * padding
        draw.text((x, y), "Current stress: " + str(val), font=font, fill="#998877")
        
        #draw.text((x, y), time.strftime("%m/%d/%Y %H:%M:%S"), font=font, fill="#FFFFFF")
        
    if val > 11:
        draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
        y = top
        draw.text((x, y), "Enough! Your day has \nended.", font=font3, fill="#0000FF")
        y -= 24 * padding
        draw.text((x, y), "Go to bed!", font=font3, fill="#00FF00")
        
    elif not buttonA.value or not buttonB.value:
        val += 1
        draw.text((x, y), "Adding Stress", font=font2, fill="#FF0000")
        if 'last_pressed' in locals() and (datetime.datetime.now() - last_pressed).total_seconds() < 5:
            y = top - 12 * padding
            draw.rectangle((0, 0, width, height), outline="#998877", fill="#FEE6E4")
            draw.text((x, y), "How about some time\nto slow down?\nLet\'s try this exercise.", font=font2, fill="#FF0000")
            disp.image(image, rotation)
            time.sleep(3)
            breathing()
            #cap = cv2.VideoCapture("BoxBreathing.mp4")
            #if (cap.isOpened()== False):
            #    print("Error opening video file")
            #while(cap.isOpened()):
            #    ret, frame = cap.read()
            #    if ret == True:
            #        cv2.imwrite("Frame:",frame)
            #f()
        last_pressed = datetime.datetime.now()

    # Display image.
    disp.image(image, rotation)
    time.sleep(1)
