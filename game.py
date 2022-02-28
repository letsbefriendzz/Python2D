import cv2
import numpy as np
import shape
import coordinate
import keyboard
import twodee

width = 800
height = 800

player = coordinate.coordinate(0.1,0.1)

def w_press(cds):
    cds.y -= 0.0015

def a_press(cds):
    cds.x -= 0.0015

def s_press(cds):
    cds.y += 0.0015

def d_press(cds):
    cds.x += 0.0015

while True:

    frame = np.zeros((height, width, 3), np.uint8)

    twodee.set_pixel(frame, player, [255,255,0], 2)

    if keyboard.is_pressed('w'):
        w_press(player)
        
    if keyboard.is_pressed('a'):
        a_press(player)

    if keyboard.is_pressed('s'):
        s_press(player)

    if keyboard.is_pressed('d'):
        d_press(player)

    if keyboard.is_pressed('esc'):
        break

    cv2.imshow('game', frame)
    cv2.waitKey(10)