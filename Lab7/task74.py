import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm # monitor resolution

#изменение разрешения с учетом соотношения изображения
def fixresize(img, max = gsm(1)-100):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), int(max))
    return cv2.resize(img, dim)

for i in range(1,7):
    crcls = 0
    img = cv2.imread(f'Lab7\\7_5_{i}.jpg')
    result = np.copy(img)

    edit = cv2.cvtColor(cv2.medianBlur(img, 55), cv2.COLOR_BGR2GRAY)
    edit = cv2.morphologyEx(edit, cv2.MORPH_CROSS, np.ones((5,5)),iterations=10)
    crcls = cv2.HoughCircles(edit, cv2.HOUGH_GRADIENT, 1, edit.shape[0], param1=200, param2=100)

    if crcls is None:
        print('ATEMP#2')
        edit = cv2.cvtColor(cv2.medianBlur(img, 25), cv2.COLOR_BGR2GRAY)
        crcls = cv2.HoughCircles(edit, cv2.HOUGH_GRADIENT, 5, edit.shape[0], param1=50, param2=100)
    
    if crcls is not None:
        print('YEEEES')
        crcls = np.uint16(np.around(crcls))
    else:print('NOOOO')

    if crcls is not None:
        for c in crcls[0, :]:
            cntr = (c[0], c[1])
            r = c[2]#*1.1
            cv2.circle(result, cntr, int(r), 0, 25)
            cv2.circle(result, cntr, int(r), (50,255,100), 15)

    if img.shape[0] > img.shape[1]:axis=1
    else:axis = 0
    img_cmb = np.concatenate((cv2.cvtColor(edit, cv2.COLOR_GRAY2BGR), result), axis)

    cv2.imshow(f'7_5_{i}_result.jpg', fixresize(img_cmb))
    key=cv2.waitKey()
    if key == ord('s'):
        cv2.imwrite(f'Lab7\\results\\7_5_{i}_result.jpg', result)
    elif key == ord('q'):
        break

    cv2.destroyAllWindows()