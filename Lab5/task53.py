import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution

#изменение разрешения с учетом соотношения изображения
def fixresize(img, max = gsm(1)/1.5-50):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), int(max))
    return cv2.resize(img, dim)

cap = cv2.VideoCapture('Lab5\\testvideo.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))*2
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('Lab5\\results\\output.mp4', fourcc, 30.0, size)
i=0
while True:
        ret, frame = cap.read()
        if not ret:
            break
        i+=1
        frame=cv2.cvtColor(255-cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),cv2.COLOR_GRAY2BGR)
        contours = cv2.Canny(cv2.blur(frame, (5,5)), 25, 100, L2gradient=False)
        cv2.imshow('test', fixresize(np.concatenate((frame, cv2.cvtColor(contours, cv2.COLOR_GRAY2BGR)), axis=1))) 
        out.write(np.concatenate((frame, cv2.cvtColor(contours, cv2.COLOR_GRAY2BGR)), axis=1))
        if cv2.waitKey(1) == ord('s'):
            cv2.imwrite(f'Lab5\\results\\sho{i}ot.jpg', np.concatenate((frame, cv2.cvtColor(contours, cv2.COLOR_GRAY2BGR)), axis=1))

cap.release() # Освобождаем ресурсы
out.release() # Освобождаем ресурсы
cv2.destroyAllWindows()