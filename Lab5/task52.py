import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution

#изменение разрешения с учетом соотношения изображения
def fixresize(img, max = gsm(1)/2-50):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), int(max))
    return cv2.resize(img, dim)

img1 = cv2.GaussianBlur(fixresize(cv2.imread('Lab5\\5-4.jpg', cv2.IMREAD_GRAYSCALE)), (3, 3), 3, 3)
img2 = cv2.GaussianBlur(fixresize(cv2.imread('Lab5\\5-5.jpg', cv2.IMREAD_GRAYSCALE)), (3, 3), 3, 3)
thres = np.copy(img2)

for i in range(0, img2.shape[0]):
    for y in range(0, img2.shape[1]):
        if img2[i,y] < 145: thres[i,y] = 135

edit1 = cv2.Canny(img1, 50, 200)
edit2 = cv2.Canny(img2, 90, 50, L2gradient=True)
edit3 = cv2.Canny(thres, 50, 135, L2gradient=True)

canny = np.concatenate((np.concatenate((img1,img2), axis=1),np.concatenate((edit1, edit2), axis=1)))
canny_exp = np.concatenate((thres, edit3))
cv2.imshow('img54&55',canny)
cv2.imshow('img55',canny_exp)
cv2.waitKey()
cv2.imwrite(f'Lab5\\results\\canny.jpg', canny)
cv2.imwrite(f'Lab5\\results\\canny_exp.jpg', canny_exp)