import numpy as np
import cv2

image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)

(h, w, c) = image.shape[:3]

M = np.float32([[1, 0, int(h//2)], [0, 1, int(w//2)]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)
