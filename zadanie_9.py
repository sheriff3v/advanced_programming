
import cv2
import imutils

image = cv2.imread("assets/catler.png")


rotated = imutils.rotate(image, 79)

cv2.imshow("Rotated by 70 Degrees", rotated)
cv2.imwrite("assets/rotated_output.jpg", rotated)
cv2.waitKey(0)