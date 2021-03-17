# Importing libraries
#import cv2
#import serial
from time import sleep
#from PIL import Image
#import os

from classes import Stage, Camera
stage = Stage("/dev/tty.usbserial-1460")
camera = Camera(0)
if __name__ == "__main__":
    stage.scan(xstart = 0, xend = 1, step_x = .1,
               ystart = 0, yend = 1, step_y = .1,
               camera = camera, invert_x=True,
               invert_y = True)


# # The app camera cannot be opened with this camera
# cap = cv2.VideoCapture(0)
# reset_zero()
# step = .5
# n_steps = 5
# for row in range(n_steps):
#     time.sleep(3)
#     move_fwd(step)
#     for col in range(n_steps):
#         move_left(step)
#         time.sleep(1)
#         # Taking a composite snapshot
#         frame = .1 * cap.read()[1]
#         for i in range(9):
#             frame += .1 * cap.read()[1] # return a single frame in variable `frame`
#         # Writing the composite image as PNG to current folder
#         cv2.imwrite('c%d_%d.png'%(row, col), frame)
#         # Converting the files to tiff and saving in ./images folder
#         Image.open('c%d_%d.png'%(row, col)).save('./images/c%d_%d.tif'%(row, col))
#         os.remove('c%d_%d.png'%(row, col))
#     # Returning to the start of the row
#     move_right(n_steps * step)
#     time.sleep(2)
#
# cap.release()
#
#
# for j in range(5):
#     images = []
#     for i in range(5):
#         image = cv2.imread("./images/c%d_%d.tif"%(i, j))
#         images.append(image)
#     stitcher = cv2.Stitcher_create()
#     (status, stitched) = stitcher.stitch(images)
#     cv2.imwrite("test%d.png"%j, stitched)