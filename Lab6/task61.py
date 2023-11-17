import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution

#изменение разрешения с учетом соотношения изображения
def fixresize(img, max = gsm(1)-100):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), int(max))
    return cv2.resize(img, dim)

original = cv2.imread('Lab6\\6-1.png', cv2.IMREAD_GRAYSCALE)
image = cv2.blur(original, (5,5))
_,image = cv2.threshold(image, 150,255, cv2.THRESH_BINARY)
image = cv2.dilate(image, np.ones((2,2)))
image = cv2.Canny(image, 50, 100)
contours,_ = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
original = cv2.cvtColor(original, cv2.COLOR_GRAY2BGR)
cv2.drawContours(image, contours, 4,(255, 51, 155))
# for contour in contours:
#     s = cv2.contourArea(contour)
#     p = cv2.arcLength(contour, True)
    
#     if s > p and p > s:
#         cv2.drawContours(original, [contour], -1,(255, 51, 155),3)
#     elif s > p and p < s:
#         cv2.drawContours(original, [contour], -1,(0, 0, 255),3)
#     else:
#         cv2.drawContours(original, [contour], -1,(0, 255, 0),3)


#cv2.imshow("Result", fixresize(np.concatenate((image, original), 0)))
cv2.imshow("Result", image)

if cv2.waitKey() == ord('s'): # Нажать 'S' чтоб сохранить файл
    cv2.imwrite('Lab6\\contours.png', image)
    cv2.imwrite('Lab6\\result.png', original)