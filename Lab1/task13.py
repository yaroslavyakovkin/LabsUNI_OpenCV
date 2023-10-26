import cv2
import numpy as np
cv2.namedWindow('test', flags=cv2.WINDOW_AUTOSIZE)
plot = np.full((150, 400, 3), 255, dtype=np.float64, order='C')
y0 = 0
purple = (255, 0, 139)
for j in range(0, 15):
    y = j * 10
    for i in range(0, 41):
        x0 = i * 10
        y0 = y
        x1 = x0 + 10
        y1 = y0 + 10
        plot[y0:y1, x0:x1] = purple
        if purple == 255:
            purple = (255, 0, 139)
        else:
            purple = 255
cv2.imshow('test', plot)
cv2.waitKey(5000)
