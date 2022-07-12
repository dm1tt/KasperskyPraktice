
import numpy as np
import math

def read_file():
    file = open("/home/dm1ttry/Рабочий стол/practice/coords.txt", "r")
    while True:
        line = file.readline()

        if not line:
            break
        
        kaif = []
        for i in range(17):
            kaif.append(file.readline())

        print(kaif)
read_file()


def take_coords():  #считывание координат положения роботаи  запись их в массив    
    coords_rob = np.array([])  #[x0, y0, x1, y1]  
    coords_dot = np.array([])  #[x0, y0]
    return coords_rob, coords_dot   


coords_rob, coords_dot = take_coords()

def moving_robot():
    a = 2

def length():
    len = math.sqrt((coords_dot[0]-coords_rob[2]) *(coords_dot[0]-coords_rob[2]) + (coords_dot[1] - coords_rob[3]) * (coords_dot[1] - coords_rob[3]))
    return len

def angle():
    alfa = math.atan((coords_rob[2] - coords_rob[0])/(coords_rob[3] - coords_rob[1]))
    phi = math.atan((coords_dot[0] - coords_rob[2])/coords_dot[1] - coords_rob[3])
    len = length()
    angle = alfa + phi

    return angle

cp = 5  #количество чекпоинтов (ввод с руки)

while (cp > 0):    #ПРОВЕРИТЬ УСЛОВИЕ ДЛЯ НАЧАЛЬНОГО ПРОБНОГО ШАГА (РАРСЧИТАТЬ В ОБЩЕМ ВИДЕ КОЛИЧЕСТВО ИТТЕРАЦИЙ)
    print(1)

    take_coords()
    angle()
    length()
    coords_rob[0] = coords_rob[2]
    coords_rob[1] = coords_rob[3]
    coords_rob[2] = coords_dot[0]
    coords_rob[3] = coords_dot[1]

    
    cp = cp - 1
  
