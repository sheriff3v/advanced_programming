
import cv2
image = cv2.imread("assets/catler.png")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (0, 0)

M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

cv2.waitKey(0)