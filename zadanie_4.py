import numpy as np
import cv2
import imutils

image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)

shifted = imutils.translate(image, 100, 50)
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)
