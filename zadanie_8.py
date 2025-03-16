
import cv2
import imutils

image = cv2.imread("assets/catler.png")


rotated = imutils.rotate(image, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
cv2.imshow("Rotated by 90 Degrees", rotated)
cv2.waitKey(0)