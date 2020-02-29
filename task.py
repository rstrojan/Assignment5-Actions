import math


def firstrun():
    return "success"


def radius_to_area(radius):
    area = math.pi * math.sqrt(radius)
    return area


def first_last(a_list):
    temp_list = []
    temp_list.append(a_list(0))
    temp_list.append(a_list(-1))
    return temp_list
