import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution

#изменение разрешения с учетом соотношения изображения
def fixresize(img, max = gsm(1)/2-50):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), int(max))
    return cv2.resize(img, dim)

#фикс собеля для правильной клетки
def fixsobel(img, xy=1, ksize=3):
    return cv2.bitwise_or(cv2.Sobel(img, -1, xy,0, ksize), 
                          cv2.Sobel(img, -1, 0,xy, ksize)) 

img1 = fixresize(cv2.imread(f'Lab5\\5-1.jpg', flags=cv2.IMREAD_GRAYSCALE))
edit1 = cv2.Sobel(img1, -1, 1, 1, 3)
edit11 = cv2.Laplacian(img1, -1)

img2 = fixresize(cv2.imread(f'Lab5\\5-2.jpg', flags=cv2.IMREAD_GRAYSCALE))
edit2 = cv2.Sobel(img2, -1, 1, 0, 7)
edit22 = cv2.Laplacian(img2, -1)

img3 = fixresize(cv2.imread(f'Lab5\\5-3.jpg', flags=cv2.IMREAD_GRAYSCALE))
edit3 = fixsobel(img3, 2)
edit33 = cv2.Laplacian(img3, -1)

img = np.concatenate((img1, img2, img3), axis=1)

edit = np.concatenate((edit1, edit2, edit3), axis=1)
sobel = np.concatenate((img, edit))
cv2.imshow('sobel', sobel)

edit = np.concatenate((edit11, edit22, edit33), axis=1)
laplacian = np.concatenate((img, edit))
cv2.imshow('laplacian', laplacian)
if cv2.waitKey() == ord('s'): 
    cv2.imwrite('Lab5\\results\\laplacian.jpg', laplacian)
    cv2.imwrite('Lab5\\results\\sobel.jpg', sobel)