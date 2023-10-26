import cv2

и = 6
img = cv2.imread('Lab2\\2-2.jpg', flags=cv2.IMREAD_GRAYSCALE)
# cv2.namedWindow('edit', flags=cv2.WINDOW_NORMAL)

thres ,edit = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Хорошо для 2-0
print(thres)
# thres ,edit = cv2.threshold(img, 95, 255, cv2.THRESH_BINARY) #Хорошо для 2-1
# edit = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 3) # Хорошо для 2-2
# thres ,edit = cv2.threshold(img, 139, 255, cv2.THRESH_BINARY) #Хорошо для 2-3
edit = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 1, 20) # Хорошо для 2-4

# thres, edit = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
# print(thres)
# thres, edit = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
# thres2, edit = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# print(thres2)

# for k in range(100, 255):
#     thres ,edit = cv2.threshold(img, k, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
#     cv2.imshow('edit', cv2.resize(edit, (int(edit.shape[1] / и), int(edit.shape[0] / и))))
#     if cv2.waitKey(100) == ord('q'):
#         break
# for k in range(901 , 1000, +50):
#     edit = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, k, 1)
#     cv2.imshow('edit', cv2.resize(edit, (int(edit.shape[1] / и), int(edit.shape[0] / и))))
#     if cv2.waitKey(100) == ord('q'):
#         break

#print(k)
cv2.imshow('edit', cv2.resize(edit, (int(edit.shape[1] / и), int(edit.shape[0] / и))))
cv2.imshow('image', cv2.resize(img, (int(img.shape[1] / и), int(img.shape[0] / и))))

cv2.waitKey()
