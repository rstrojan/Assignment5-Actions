import math
from datetime import datetime


def firstrun():
    return "success"


def radius_to_area(radius):
    area = math.pi * (radius*radius)
    return round(area, 2)


def time_delta(date1, date2):
    d1 = datetime.strptime(date1, "%m/%d/%Y")
    d2 = datetime.strptime(date2, "%m/%d/%Y")
    return abs(d2-d1).days


def first_last(a_list):
    temp_arr = []
    temp_arr.append(a_list[0])
    temp_arr.append(a_list[-1])
    return temp_arr