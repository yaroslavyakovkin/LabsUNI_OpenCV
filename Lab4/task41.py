import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution

def fixresize(img, max):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), max)
    return cv2.resize(img, dim)

axis = 0
img = cv2.imread('Lab4\\4-1.jpg', flags=cv2.IMREAD_GRAYSCALE)
 
if img.shape[0] > img.shape[1]:axis=1
img_combine = np.concatenate((img, imgf), axis)
   
cv2.imshow(f'Two of us', fixresize(img_combine, gsm(1)-100))
if cv2.waitKey() == ord('s'):
    cv2.imwrite(f'filtred\{type}_4-1.jpg', img_combine)
cv2.destroyAllWindows()