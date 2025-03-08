import cv2

image = cv2.imread("./assets/bird.jpg")
cv2.imshow("before", image)
(h, w) = image.shape[:2]

image[0, w - 1] = (0, 0, 255)

(b, g, r) = image[0, w - 1]
print("Pixel at (0, w-1) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.imshow("after", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
