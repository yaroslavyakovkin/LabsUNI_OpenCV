import cv2, math
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution

def draw_line(rho, theta, img, color=(100, 0, 255), thickness=3):
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    x0 = cos_t * rho
    y0 = sin_t * rho
    pt1 = int(x0 - 1000 * sin_t), int(y0 + 1000 * cos_t)
    pt2 = int(x0 + 1000 * sin_t), int(y0 - 1000 * cos_t)
    cv2.line(img, pt1, pt2, color, thickness)

#изменение разрешения с учетом соотношения изображения
def fixresize(img, max = gsm(1)-100):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), int(max))
    return cv2.resize(img, dim)

cap = cv2.VideoCapture('Lab5\\testvideo.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/3)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/3)
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('Lab7\\results\\output.mp4', fourcc, 30.0, size)
i=0
float(i)
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(int(frame.shape[1]/3), int(frame.shape[0]/3)))
    if not ret:
        break
    i+=0.1
    frame=cv2.cvtColor(255-cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),cv2.COLOR_GRAY2BGR)
    contours = cv2.Canny(cv2.blur(frame, (5,5)), 25, 100, L2gradient=False)
    lines = cv2.HoughLines(contours, 1.5, np.pi/45, 50)
    edit = np.copy(frame)
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            draw_line(rho, theta, edit)
    
    cv2.imshow('test', fixresize(edit)) 
    out.write(edit)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite(f'Lab7\\results\\sho{i}ot.jpg', np.concatenate((frame, edit), axis=1))
    elif key == ord('q'):
        break

cap.release() # Освобождаем ресурсы
out.release() # Освобождаем ресурсы
cv2.destroyAllWindows()