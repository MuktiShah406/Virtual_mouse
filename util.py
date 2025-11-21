import numpy as np
import math

def get_angle(a, b, c):
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degrees(radians))
    if angle > 180:
        angle = 360 - angle
    return angle

def get_distance(p1, p2):  # ← two parameters!
    x1, y1 = p1
    x2, y2 = p2
    dist = math.hypot(x2 - x1, y2 - y1)
    return np.interp(dist, [0, 1], [0, 1000])
