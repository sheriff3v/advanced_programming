import cv2
import imutils

image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)

x = int(input("Podaj X: "))
y = int(input("Podaj Y: "))

shifted = imutils.translate(image, x, y)
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)
