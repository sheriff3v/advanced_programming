import cv2

image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)

height, width, _ = image.shape

right_half = image[:, width//2:]

flipped_right_half = cv2.flip(right_half, 1)

image[:, width//2:] = flipped_right_half

cv2.imshow("Image with Flipped Region", image)

cv2.waitKey(0)
