import cv2

image = cv2.imread("./assets/cat.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imwrite("./assets/sad_cat.jpg", image)
