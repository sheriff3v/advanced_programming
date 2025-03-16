import cv2
import imutils

image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w * 0.2, h * 0.2)

resized = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized", resized)
cv2.waitKey(0)