import cv2

image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)
flipped = cv2.flip(image, 1)
flipped = cv2.flip(flipped,0)
cv2.imshow("Flipped both", flipped)

cv2.waitKey(0)