import cv2
# load the original input image and display it to our screen
image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)
# flip the image horizontally
print("[INFO] flipping image horizontally...")
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

cv2.waitKey(0)