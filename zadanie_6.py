
import cv2
import imutils

image = cv2.imread("assets/catler.png")


rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)