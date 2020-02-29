import math


def firstrun():
    return "success"


def radius_to_area(radius):
    area = math.pi * (radius*radius)
    return round(area, 2)
