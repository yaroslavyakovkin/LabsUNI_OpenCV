import cv2
from numpy import copy

img = cv2.imread('Lab8\\task.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gran = copy(gray)
for i in range(0, gray.shape[0]):
    for y in range(0, gray.shape[1]):
        if gray[i,y] < 255: 
            gran[i,y] = 0
            gray[i,y] = 200

gray=cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cntrs,h = cv2.findContours(gran, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
main=h[0][0][2]
draft=cv2.moments(cntrs[main])

for i in cntrs:
    moment = cv2.moments(i)
    moment_hu=cv2.HuMoments(moment)
    if (draft['m00']>=0.99*moment['m00'] and draft['m00']<=1.01*moment['m00']) and not\
        (draft['nu20']>=0.99*moment['nu20'] and draft['nu20']<=1.01*moment['nu20']):
        cv2.drawContours(gray, [i], -1, (125, 0, 255), thickness=2)

cv2.imshow('Result', gray)
if cv2.waitKey() == ord('s'):
    cv2.imwrite('Lab8\\result.jpg', gray)