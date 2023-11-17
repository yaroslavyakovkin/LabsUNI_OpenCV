import cv2
import numpy as np
from win32api import GetSystemMetrics as gsm  # monitor resolution


# изменение разрешения с учетом соотношения изображения
def fixresize(img, max=gsm(1) - 100):
    r = max / img.shape[0]
    dim = (int(img.shape[1] * r), int(max))
    return cv2.resize(img, dim)


original = cv2.imread("Lab6\\6-1.png", cv2.IMREAD_GRAYSCALE)
# Подготовка изображения.
image = cv2.blur(original, (5, 5))
_, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
image = cv2.dilate(image, np.ones((2, 2)))
image = cv2.Canny(image, 50, 100)
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Конвертация для добавления цвета и конкатенации.
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
original = cv2.cvtColor(original, cv2.COLOR_GRAY2BGR)

# Проходим по всем контурам
for contour in contours:
    s = cv2.contourArea(contour)
    p = cv2.arcLength(contour, True)

    _, _, h, w = cv2.boundingRect(contour)
    _, r = cv2.minEnclosingCircle(contour)

    s_circle = (p * r) / 2  # Это плохо
    s_rect = w * h  # Тут норм

    # Круг или квадрат?
    if int(s_circle - s) < int(s_rect - s):
        cv2.drawContours(original, [contour], -1, (255, 50, 50), 3)
    # Это квадрат?
    elif int(s_rect - s) < 1000:
        cv2.drawContours(original, [contour], -1, (50, 50, 255), 3)
    # Ну теперь точно треугольник.
    else:
        cv2.drawContours(original, [contour], -1, (255, 50, 155), 3)

# Выводим на экран и сохраняем.
cv2.imshow("Result", fixresize(np.concatenate((image, original), 0)))
if cv2.waitKey() == ord("s"):  # Нажать 'S' чтоб сохранить файл
    cv2.imwrite("Lab6\\contours.png", image)
    cv2.imwrite("Lab6\\result.png", original)
