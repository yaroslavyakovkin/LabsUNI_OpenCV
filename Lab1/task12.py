import cv2
import numpy as np
plot = np.full((500, 500, 3), 255, dtype=np.uint8, order='C')
plot = cv2.circle(plot, (400, 400), 50, (20, 0, 255), 2)
plot = cv2.putText(plot, 'circle', (360, 405), cv2.FONT_ITALIC, 1, 0, 1)
plot = cv2.rectangle(plot, (50, 40), (210, 120), (255, 0, 139), 2, 0)
plot = cv2.putText(plot, 'rectangle', (60, 90), cv2.FONT_ITALIC, 1, 0, 1)
plot = cv2.line(plot, (0, 500), (500, 0), (255, 170, 66), 3)
plot = cv2.putText(plot, 'line', (230, 250), cv2.FONT_ITALIC, 1, 0, 1)
cv2.namedWindow('test', flags=cv2.WINDOW_AUTOSIZE)
cv2.imshow('test', plot)
cv2.waitKey(0)