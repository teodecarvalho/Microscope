# Importing libraries
import cv2
import serial
import time
from PIL import Image
import os

# Setting up the microscope stage
stage = serial.Serial('COM4', 115200, timeout=3)
time.sleep(2)
stage.write(b"\r\n\r\n")

# Defining functions
def send_gcode_str(gcode_str):
    stage.flushInput()
    time.sleep(.01)
    print(gcode_str)
    gcode_str += "\n"
    stage.write(gcode_str.encode())
    grbl_out = stage.readline()  # Wait for robot response with carriage return
    print(grbl_out.strip())
    return (grbl_out.strip().decode("ascii"))


def reset_zero():
    send_gcode_str("G10 P0 L20 X0 Y0 Z0")


def return_to_zero():
    send_gcode_str("G90 G0 Z1.0")
    send_gcode_str("G90 G0 X0 Y0 Z0")

def move_left(step_size):
    send_gcode_str("G21 G91 G0 X-" + str(step_size))
    send_gcode_str("G90")

def move_right(step_size):
    send_gcode_str("G21 G91 G0 X" + str(step_size))
    send_gcode_str("G90")

def move_fwd(step_size):
    send_gcode_str("G21 G91 G0 Y" + str(step_size))
    send_gcode_str("G90")

def move_rev(step_size):
    send_gcode_str("G21 G91 G0 Y-" + str(step_size))
    send_gcode_str("G90")

def move_up(step_size):
    send_gcode_str("G21 G91 G0 Z" + str(step_size))
    send_gcode_str("G90")

def move_down(step_size):
    send_gcode_str("G21 G91 G0 Z-" + str(step_size))
    send_gcode_str("G90")

# The app camera cannot be opened with this camera
cap = cv2.VideoCapture(0)
reset_zero()
step = .5
n_steps = 5
for row in range(n_steps):
    time.sleep(3)
    move_fwd(step)
    for col in range(n_steps):
        move_left(step)
        time.sleep(1)
        # Taking a composite snapshot
        frame = .1 * cap.read()[1]
        for i in range(9):
            frame += .1 * cap.read()[1] # return a single frame in variable `frame`
        # Writing the composite image as PNG to current folder
        cv2.imwrite('c%d_%d.png'%(row, col), frame)
        # Converting the files to tiff and saving in ./images folder
        Image.open('c%d_%d.png'%(row, col)).save('./images/c%d_%d.tif'%(row, col))
        os.remove('c%d_%d.png'%(row, col))
    # Returning to the start of the row
    move_right(n_steps * step)
    time.sleep(2)

cap.release()


for j in range(5):
    images = []
    for i in range(5):
        image = cv2.imread("./images/c%d_%d.tif"%(i, j))
        images.append(image)
    stitcher = cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)
    cv2.imwrite("test%d.png"%j, stitched)