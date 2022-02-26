import random
from tarfile import PAX_FIELDS
import shape
import cv2
import imageio
import numpy as np

width = 500
height = 500

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
            if x < width and y < height:
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

def main():
    cds = shape.square()

    # init shape with 50 random coords
    pixel_color = [255,255,255]

    # frames array to store all frames generated and return a gif
    frames = []

    # i to iterate over x
    i = 0
    x = 376
    j = x/2
    # make x many modifications to the image
    while i < x:
        # init new img, all black
        img = np.zeros((height, width, 3), np.uint8)

        # sets our coordinates to white
        for cd in cds.coordinates:
            set_pixel(img, cd, pixel_color, stroke=1)

        for cd in cds.get_medians().coordinates:
            set_pixel(img, cd, [150,100,200], stroke=1)

        for cd in cds.get_medians().get_medians().coordinates:
            set_pixel(img, cd, [0,255,255], stroke=0.5)

        for cd in cds.get_medians().get_medians().get_medians().coordinates:
            set_pixel(img, cd, [0,0,255], stroke=0.5)

        for cd in cds.get_medians().get_medians().get_medians().get_medians().coordinates:
            set_pixel(img, cd, [0,255,0], stroke=0.5)

        set_pixel(img, cds.get_median(), [255,0,0], stroke=1)

        # generates median coordinates, sets those to white

        frames.append(img)

        if i < x:
            if i < j / 2:
                cds.coordinates[0].x -= 0.0015
                cds.coordinates[0].y -= 0.0015
                cds.coordinates[2].x += 0.0015
                cds.coordinates[2].y += 0.0015
            elif i < j:
                cds.coordinates[0].x += 0.0015
                cds.coordinates[0].y += 0.0015
                cds.coordinates[2].x -= 0.0015
                cds.coordinates[2].y -= 0.0015
            elif i > j and i < j + ( j / 2 ):
                cds.coordinates[1].x -= 0.0015
                cds.coordinates[1].y -= 0.0015
                cds.coordinates[3].x += 0.0015
                cds.coordinates[3].y += 0.0015
            else:
                cds.coordinates[1].x += 0.0015
                cds.coordinates[1].y += 0.0015
                cds.coordinates[3].x -= 0.0015
                cds.coordinates[3].y -= 0.0015
            
        print(i)
        i += 1
    
    for frame in frames:
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

    imageio.mimsave('F:\\test.gif', frames, fps=60)

# CALL MAIN
main()

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


"""
PENTAGONAL MANIPULATION

        for cd in cds.get_medians().coordinates:
            set_pixel(img, cd, rgb=[0,0,255], stroke=1)

        for cd in cds.get_medians().get_medians().coordinates:
            set_pixel(img, cd, rgb=[0,255,0], stroke=1)

        if i < x / 2:
            cds.coordinates[0].x -= 0.0025
            cds.coordinates[4].x -= 0.0025

            cds.coordinates[0].y -= 0.0025
            cds.coordinates[4].y -= 0.0025
        else:
            cds.coordinates[0].x += 0.0025
            cds.coordinates[4].x += 0.0025

            cds.coordinates[0].y += 0.0025
            cds.coordinates[4].y += 0.0025
"""