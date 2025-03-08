import cv2

image = cv2.imread("./assets/cat.jpg")
cv2.namedWindow("cat", cv2.WINDOW_NORMAL)
cv2.imshow("cat", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

