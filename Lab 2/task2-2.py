import cv2

i = 0
b = 0
k = 0
cv2.namedWindow('frame', flags=cv2.WINDOW_AUTOSIZE)
cam = cv2.VideoCapture(1)
while True:
    for k in range(3 , 1000, +10):
        ret, frame = cam.read()
        frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_LANCZOS4)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, k, 1)
        # frame2 = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        # i += 120
        # b -= 60
        # k += 30
        # frame2[frame == 0] = (i, b, k)
        # for i in range(0, 100):
        #     frame = cv2.putText(frame, '17.09.2023', (900 + i, 700 + i), cv2.FONT_ITALIC, 2, 0 + i * 2, 3)
        # frame = cv2.putText(frame, '17.09.2023', (900, 700), cv2.FONT_ITALIC, 2, 255, 1)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            exit()