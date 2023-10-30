import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm  # monitor resolution


def fixresize(img, max):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), max)
    return cv2.resize(img, dim)

def morph(image, method, kernel):
    s = 0
    for i in range(2):
        if method.lower() == "размыкание" or s == 1:
            new = cv2.erode(image, kernel, None, None, 5)
            s , method = (2,'')
        elif method.lower() == "замыкание" or s == 2:
            new = cv2.dilate(image, kernel, None, None, 5)
            s , method = (1,'')
    return new
        
#method = 'замыкание'            
method = 'размыкание'           
k = np.ones((2, 2), np.uint8)
axis = 0
img = cv2.imread("Lab4\\4-1.jpg")
#tres, imgt = cv2.threshold(img, 255/2, 255, cv2.THRESH_BINARY)
img_new = morph(img, method, k)
img_new2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, k, None, 5) 

if img.shape[0] > img.shape[1]:
    axis = 1
img_combine = np.concatenate((img, img_new, img_new2), axis)

cv2.imshow(f"edited", fixresize(img_combine, gsm(1) - 50))
if cv2.waitKey() == ord("s"):
    cv2.imwrite(f"Lab4\\morph\\2_4-1.jpg", img_combine)