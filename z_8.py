import cv2

image = cv2.imread("./assets/bird.jpg")
(h, w) = image.shape[:2]
y = 100

image[y, 0:w] = (0,255,0)
cv2.imshow("after",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

