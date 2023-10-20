import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution

def fixresize(img, max):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), max)
    return cv2.resize(img, dim)

axis = 0
img = cv2.imread('Lab3\\3-3.jpg', flags=cv2.IMREAD_ANYCOLOR)

for k in range(3,101,2):
    #imgf = cv2.blur(img, (k, k))
    #imgf = cv2.boxFilter(img, -1, (k,k))
    #imgf = cv2.medianBlur(img, k) #3-2(15) 3-1(35)
    #imgf = cv2.GaussianBlur(img, (k, k), k*3, k*3)__
    #imgf = cv2.bilateralFilter(img, k, k*2 , k*2) #3-1
    imgf = cv2.filter2D(img, -1, np.ones((k,k),np.float32)/k**2) #3-2(20,50) 3-1(50,50)
    
    if img.shape[0] > img.shape[1]:axis=1
    img_combine = np.concatenate((img, imgf), axis)
    
    cv2.imshow('3-3.jpg', fixresize(img_combine, gsm(1)-100))
     
    if cv2.waitKey(100) != -1:
        if cv2.waitKey() == ord('s'):
            cv2.imwrite(f'Lab3\\filtred\\{k}_3-3.jpg', img_combine)
            break
        else:
            break