import cv2

image_1 = cv2.imread("./assets/cat.jpg")
image_2 = cv2.imread("./assets/cat_2.jpg")

cv2.imshow("cat_1",image_1)
cv2.imshow("cat_2", image_2)

cv2.waitKey(0)
cv2.destroyAllWindows()
