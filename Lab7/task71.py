import cv2, math
import numpy as np
def draw_line(rho, theta, img, color=(255, 255, 255), thickness=5):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x0 = cos_t * rho
    y0 = sin_t * rho
    pt1 = int(x0 - 1000 * sin_t), int(y0 + 1000 * cos_t)
    pt2 = int(x0 + 1000 * sin_t), int(y0 - 1000 * cos_t)
    cv2.line(img, pt1, pt2, color, thickness)

#подготовка изобрадения
edit = cv2.imread('Lab7\\7_1.jpg')
img=cv2.cvtColor(edit,cv2.COLOR_BGR2GRAY)
_,img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
lines = cv2.HoughLines(img, 1.51, np.pi/180, int(img.shape[0]))

for line in lines:
    rho, theta = line[0]
    draw_line(rho, theta, edit)

cv2.imshow('orig',img)
cv2.imshow('edit',edit)

if cv2.waitKey() == ord('s'):
    cv2.imwrite('Lab7\\results\\7_1_edited.jpg',edit)