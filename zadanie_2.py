import cv2

image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

cv2.waitKey(0)