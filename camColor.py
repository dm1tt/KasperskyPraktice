import cv2 
import numpy as np

def write_file(cent):    
    file = open("/home/dm1ttry/Рабочий стол/practice/coords.txt", "a")
    file.write(str(cent) + '\n')
    file.close()

def cont():
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, left, right)      #создание и отрисовка контура
    contours, hierarchy = cv2.findContours( thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours

def center():
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    center = (int(rect[0][0]),int(rect[0][1]))
    area = int(rect[1][0]*rect[1][1])
    write_file(center)
    return center, area, box

def coords():
    cv2.drawContours(img,[box],0,(255, 0, 0),2)
    cv2.circle(img, cent, 2, (0, 0, 128), 2)
    text = "(" + str(cent[0]) + ", " + str(cent[1]) + ")"
    cv2.putText(img, text, (cent[0] + 10, cent[1] + 10), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 128), 1, 8, 0)

if __name__ == '__main__':
    cv2.namedWindow( "camera" ) #создание окна
    cap = cv2.VideoCapture(0)

    left = np.array((90, 55, 10), np.uint8)
    right = np.array((132, 255, 255), np.uint8)

    while True:
        flag, img = cap.read()
        img = cv2.flip(img,1)
        try:

            for cnt in cont():
                  
                cent, ar, box = center()

                if ar > 1000: #вывод координат на изображение 
                    coords()                     

            cv2.imshow('camera', img)

        except:
            cap.release()
            raise
        butt = cv2.waitKey(5)
        if butt == 27:          #клавиша ECS ля выхода
            break

    cap.release()
    cv2.destroyAllWindows()
