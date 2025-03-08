import cv2

image = cv2.imread("./assets/cat.jpg")
false_path = cv2.imread("./assert/dog.mp4")

cv2.imshow("test",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

