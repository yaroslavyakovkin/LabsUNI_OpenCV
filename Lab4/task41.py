import cv2
import numpy as np


def morph(image, method, kernel, iterations):
    s = 0
    for i in range(2):
        if method == "open" or s == 1:
            new = cv2.erode(image, kernel, None, None, iterations)
            s , method = (2,'')
        elif method == "close" or s == 2:
            new = cv2.dilate(image, kernel, None, None, iterations)    
            s , method = (1,'')
        image = new
    return image

methods = {'close':cv2.MORPH_CLOSE, 'open':cv2.MORPH_OPEN}
method = input('''1.Замыкание
2.Размыкание
Номер требуемой операции: ''')
if method == '1': method = 'close'  
elif method == '2': method = 'open'

f = cv2.FONT_ITALIC
img = 255 - cv2.imread("Lab4\\4-1.jpg")   
i = 5
k = np.ones((2, 2))
c = (255, 255, 255)
img_new = morph(img, method, k, i)
img_new2 = cv2.morphologyEx(img, methods[method], k, None, None, i)
img_diff = cv2.absdiff(img_new, img_new2)
img_diff = cv2.dilate(img_diff, k)

img_combine = 255 - np.concatenate((cv2.putText(img, 'original', (30,30), f, 1,c,1),
                              cv2.putText(img_new, 'my func', (30,30), f, 1,c,1),
                              cv2.putText(img_new2, 'cv2 func', (30,30), f, 1,c,1),
                              cv2.putText(img_diff, 'difference', (30,30), f, 1,c,1)),1)

cv2.imshow(f"{method}", img_combine)
if cv2.waitKey() == ord("s"):
    cv2.imwrite(f"Lab4\\morph\\{method}-{i}_4-1.jpg", img_combine)