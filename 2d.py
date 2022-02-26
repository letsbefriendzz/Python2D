import random
import shape
import cv2
import numpy as np

width = 1000
height = 1000

def set_pixel(image, cd, rgb=[255,255,255], stroke=0):

    # sometimes we have a trailing deicmal, get rid of it if need be
    x = int( (cd.x * width) )
    y = int( (cd.y * height) )

    #origin x and y
    o_x = int( (cd.x * width) )
    o_y = int( (cd.y * height) )
    
    # iterate over pixels, flipping each, to create a square
    while y - stroke <= (o_y +stroke):
        x = o_x
        while x - stroke <= (o_x +stroke):
            image[y][x][0] = rgb[0]
            image[y][x][1] = rgb[1]
            image[y][x][2] = rgb[2]
            x += 1
        y += 1

# mutliply decimal by width coordinate
def get_x_coordinate(decimal):
    return int( width * decimal )

def get_y_coordinate(decimal):
    return int( (1 - decimal) * height )

# new shape object
cds = shape.shape()

for cd in shape.pentagon:
    cds.add(cd.x, cd.y)

angles = shape.relative_angles(cds.get_median(), cds)

i = 0
x = 100

# make x many modifications to the image
while i < x:

    # init new img, all black
    img = np.zeros((height, width, 3), np.uint8)

    # sets our coordinates to white
    for cd in cds.coordinates:
        set_pixel(img, cd, rgb=[255,255,255], stroke=1)

    for cd in cds.get_medians().coordinates:
        set_pixel(img, cd, rgb=[0,0,255], stroke=1)

    for cd in cds.get_medians().get_medians().coordinates:
        set_pixel(img, cd, rgb=[0,255,0], stroke=1)

    md = cds.get_median()
    set_pixel(img, md, rgb=[255,0,0], stroke=1.5)

    # generates median coordinates, sets those to white

    cds.coordinates[0].x -= 0.0025
    cds.coordinates[4].x -= 0.0025

    cds.coordinates[0].y -= 0.0025
    cds.coordinates[4].y -= 0.0025

    cv2.imshow('img', img)
    cv2.waitKey(50)
    i += 1

cv2.imshow('img',img)
cv2.waitKey(5000)

"""
STAR
    # generates median coordinates, sets those to white
    for cd in cds.get_medians().get_medians().get_medians().get_medians().get_medians().coordinates:
        img[int(cd.y * height)][int(cd.x * width)][0] = 255
        img[int(cd.y * height)][int(cd.x * width)][1] = 255
        img[int(cd.y * height)][int(cd.x * width)][2] = 255

    for cd in cds.get_medians().get_medians().coordinates:
        img[int(cd.y * height)][int(cd.x * width)][0] = 255
        img[int(cd.y * height)][int(cd.x * width)][1] = 255
        img[int(cd.y * height)][int(cd.x * width)][2] = 255
"""