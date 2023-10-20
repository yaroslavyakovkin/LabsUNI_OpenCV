import cv2

img = cv2.imread('Lab3\\3-4.jpg')

border_types = {
    'CONSTANT': cv2.BORDER_CONSTANT,
    'REPLICATE': cv2.BORDER_REPLICATE,
    'REFLECT': cv2.BORDER_REFLECT,
    'WRAP': cv2.BORDER_WRAP,
    'REFLECT_101': cv2.BORDER_REFLECT_101,
    'ISOLATED': cv2.BORDER_ISOLATED
}

for border, types in border_types.items():
    bord = cv2.copyMakeBorder(img, 500,1500,1000,2000, types, None, value=(100, 100, 100))
    cv2.imwrite(f'Lab3\\bordered\\{border}_3-4.jpg', bord)