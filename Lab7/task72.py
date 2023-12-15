import cv2
import numpy as np

def draw_line_P(x0, y0, x1, y1, img, color=(125, 0, 255), thickness=3):
    cv2.line(img, (x0, y0), (x1, y1),color, thickness)

i=0
cap = cv2.VideoCapture('Lab5\\testvideo.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('Lab7\\results\\output.mp4', fourcc, 30.0, size)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame=cv2.cvtColor(255-cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),cv2.COLOR_GRAY2BGR)

    cntrs = cv2.Canny(cv2.blur(frame, (5,5)), 25, 100, L2gradient=False)
    cntrs = cv2.morphologyEx(cntrs,cv2.MORPH_CLOSE,np.ones((3,5)), iterations=3)
    cntrs = cv2.dilate(cntrs,np.ones((5,3)), iterations=2)

    lines = cv2.HoughLinesP(cntrs, 1, np.pi/180, 200, 50, 20)
    edit = np.copy(frame)
    
    if lines is not None:
        for line in lines:
            a, b, c, d = line[0]
            draw_line_P(a, b, c, d, edit)
    
    cv2.imshow('test', edit)
    out.write(edit)

    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite(f'Lab7\\results\\sho{int(i)}ot.jpg', np.concatenate((frame, cntrs, edit), axis=1))
        i+=1
    elif key == ord('q'):
        break

cap.release() # Освобождаем ресурсы
out.release() # Освобождаем ресурсы
cv2.destroyAllWindows()