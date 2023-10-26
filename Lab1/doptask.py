import cv2
cv2.namedWindow('frame', flags=cv2.WINDOW_AUTOSIZE)
cam = cv2.VideoCapture(1)
while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTERSECT_PARTIAL)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for i in range(0,100):
        frame = cv2.putText(frame, '17.09.2023', (900+i, 700+i), cv2.FONT_ITALIC, 2, 0+i*2, 3)
    frame = cv2.putText(frame, '17.09.2023', (900, 700), cv2.FONT_ITALIC, 2, 255, 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break