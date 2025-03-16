import cv2
import imutils

image = cv2.imread("assets/catler.png")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 60 Degrees, warpAffine", rotated)

imutils = imutils.rotate(image, 60)
cv2.imshow("Rotated by 60 Degrees, imutils", imutils)
cv2.waitKey(0)