import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution

def fixresize(img, max):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), max)
    return cv2.resize(img, dim)

i = 2
file = f'3-{i}.PNG'
axis = 0
flags = {'COLOR': cv2.IMREAD_COLOR, 'GRAY': cv2.IMREAD_GRAYSCALE}
for type, flag  in flags.items():
    img = cv2.imread(file, flag)

    imgf = cv2.blur(img, (50, 50), None, (10, 10))
    #imgf = cv2.boxFilter(img, -1, (80,80))
    #imgf = cv2.medianBlur(img, 15) #3-2(15) 3-1(35)
    #imgf = cv2.GaussianBlur(img, (41, 41), 1000, 100)
    #imgf = cv2.bilateralFilter(img, 40, 300, 500) #3-1
    #imgf = cv2.filter2D(img, -1, np.ones((50,50),np.float32)/2500) #3-2(20,50) 3-1(50,50)
    
    if img.shape[0] > img.shape[1]:axis=1
    img_combine = np.concatenate((img, imgf), axis)
    
    cv2.imshow(f'{type}_{file}', fixresize(img_combine, gsm(1)-100))
    if cv2.waitKey() == ord('s'):
            cv2.imwrite(f'filtred\{type}_{file}', img_combine)
    cv2.destroyAllWindows()