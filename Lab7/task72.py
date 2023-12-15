import cv2, math
import numpy as np

_, img = cv2.threshold(cv2.imread("Lab4\\4-1.jpg", cv2.IMREAD_GRAYSCALE), 50, 255, cv2.THRESH_BINARY_INV)
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((2,2)),iterations=2)
k = int(img.shape[0]/4)
lines = cv2.HoughLinesP(img, 1, np.pi/180, k)
crcls = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, k, param2=30)
crcls = np.uint16(np.around(crcls))

img = 255 - cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

lngt2=0
for line in lines:
    a1, b1, c1, d1 = line[0]
    lngt1 = math.sqrt((a1-c1)**2 + (b1-d1)**2)
    if lngt1 > lngt2:
        lngt2 = lngt1
        a2, b2, c2, d2 = (a1,b1,c1,d1)
cv2.line(img, (a2, b2), (c2, d2), (125,0,255), 3)

r2=0
for i in crcls[0, :]:
    r1 = i[2]
    if r1 > r2:
        cntr = (i[0], i[1])
        r2 = r1
cv2.circle(img, cntr, r2, (255,0,125), 3)

cv2.imshow('result',img)
if cv2.waitKey() == ord('s'):
    cv2.imwrite('Lab7\\results\\7_2_result.jpg', img)