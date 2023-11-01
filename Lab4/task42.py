import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution


def fixresize(img, max):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), max)
    return cv2.resize(img, dim)

f = cv2.FONT_ITALIC
k1 = np.ones((2,2))
k2 = np.ones((2,1))
k3 = np.ones((1,2))
c = 0

img  = cv2.imread('Lab4\\4-2.jpg', flags=cv2.IMREAD_GRAYSCALE)
#img = cv2.blur(img, (2,2))
t, imgbt = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
imgbt = cv2.morphologyEx(imgbt, cv2.MORPH_CLOSE, k1)
imgbt = cv2.erode(imgbt, k2, None, (0,0), 3)
imgbt = cv2.erode(imgbt, k3, None, (1,0), 1)

img_combine = np.concatenate((cv2.putText(img, 'original', (30,30), f, 1,c,2),
                            cv2.putText(imgbt, 'noise reduce', (30,30), f, 1,c,2)),1)

cv2.imshow('kod', fixresize(img_combine, gsm(1)-100))
cv2.imwrite('Lab4\\mrph\\final_4-2.jpg', img_combine)
cv2.waitKey()