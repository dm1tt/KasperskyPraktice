import json
import numpy as np
import math
from camColor import calc

cam = calc()

def read_to_array():
    json_data = read_file()
    array_of_points = []
    for i in range(len(json_data)):
        array_of_points.append(json_data[i]['point'])
    return array_of_points


def read_file():
    file = cam.json_data
    return file

cam.show()
print(read_to_array())

array = read_to_array()
print(array[0][1])

for i in range(len(array) - 1):

    i -= 1


def length():
    len = math.sqrt((array[i+1][i]-array[i][i])**2 +(array[i+1][i+1]-array[i][i+1])**2)
    return len

def angle():
    #alfa = math.atan((coords_rob[2] - coords_rob[0])/(coords_rob[3] - coords_rob[1]))
    phi = math.atan((array[i+1][i]-array[i][i])/(array[i+1][i+1]-array[i][i+1]))  #угол между вертикалью и стикером
    len = length()
    angle = alfa + phi

    return angle
"""
cp = 5  #количество чекпоинтов (ввод с руки)

while (cp > 0):    #ПРОВЕРИТЬ УСЛОВИЕ ДЛЯ НАЧАЛЬНОГО ПРОБНОГО ШАГА (РАРСЧИТАТЬ В ОБЩЕМ ВИДЕ КОЛИЧЕСТВО ИТТЕРАЦИЙ)
    print(1)

    take_coords()
    angle()
    length()
    cp = cp - 1
    """