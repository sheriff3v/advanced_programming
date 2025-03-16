
import cv2
import imutils

image = cv2.imread("assets/catler.png")


rotated = imutils.rotate(image, 0)
for i in range (24):
    rotated = imutils.rotate(image, 15 * i)
    cv2.imshow(f"Rotated by 15 Degrees: {i} times", rotated)
    cv2.waitKey(500)


cv2.imshow("Rotated by 90 Degrees", rotated)
cv2.waitKey(0)