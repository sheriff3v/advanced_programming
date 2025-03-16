import cv2
image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)
flippedH = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flippedH)

flippedV = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flippedV)

flippedB = cv2.flip(flippedH,0)
cv2.imshow("Flipped both", flippedB)



cv2.waitKey(0)