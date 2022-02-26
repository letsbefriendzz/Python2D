import math
import numpy as np

def CCW_2D_ROTATION(angle):
    m = np.array([ [math.cos(angle), -(math.sin(angle))], [math.cos(angle), math.sin(angle)] ])
    return m

def MATRIX_2D(x,y):
    m = np.array([ [0,x], [0,y] ])
    return m