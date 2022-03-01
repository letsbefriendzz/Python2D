from pydoc import cli
import cv2
import numpy as np
import shape
import coordinate
import keyboard
import twodee
import pong_networking
import socket
import sys

width = 800
height = 800

paddle1 = shape.shape()
paddle1.add(0.1,0.1)
paddle1.add(0.1,0.2)

paddle2 = shape.shape()
paddle2.add(0.9,0.1)
paddle2.add(0.9,0.2)

def w_press(cds):
    for cd in cds.coordinates:
        cd.y -= 0.005

def a_press(cds):
    pass

def s_press(cds):
    for cd in cds.coordinates:
        cd.y += 0.005

def d_press(cds):
    pass

def get_paddle_coordinates(paddle):
    return str(paddle.coordinates[0].y)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if sys.argv[1] == 'server':
    sock.bind( ( pong_networking.localip, pong_networking.localport ) )

while True:

    if sys.argv[1] == 'server':
        bapair = sock.recvfrom(pong_networking.bufferSize)
        server_msg = bapair[0]
        adr = bapair[1]
        print(server_msg)
        paddle2.coordinates[0].y = float(server_msg.decode())
        paddle2.coordinates[1].y = float(server_msg.decode()) + 0.1
    elif sys.argv[1] == 'client':
        sock.sendto(get_paddle_coordinates(paddle1).encode(), ( pong_networking.localip, pong_networking.localport ) )
    else:
        print("invalid networking data")
        break

    frame = np.zeros((height, width, 3), np.uint8)

    p1a = paddle1.coordinates[0]
    p1b = paddle1.coordinates[1]

    for cd in paddle1.coordinates:
        twodee.set_pixel(frame, cd, [255,255,255], 2)

    for cd in paddle2.coordinates:
        twodee.set_pixel(frame, cd, [255,255,255], 2)

    if keyboard.is_pressed('w'):
        w_press(paddle1)

    if keyboard.is_pressed('a'):
        a_press(paddle1)

    if keyboard.is_pressed('s'):
        s_press(paddle1)

    if keyboard.is_pressed('d'):
        d_press(paddle1)

    if keyboard.is_pressed('esc'):
        break

    if sys.argv[1] == 'server':
        sock.sendto(get_paddle_coordinates(paddle1).encode(), adr)

    elif sys.argv[1] == 'client':
        client_msg = sock.recvfrom(pong_networking.bufferSize)[0]
        paddle2.coordinates[0].y = float(client_msg.decode())
        paddle2.coordinates[1].y = float(client_msg.decode()) + 0.1
        print(client_msg)

    cv2.imshow('game', frame)
    cv2.waitKey(10)