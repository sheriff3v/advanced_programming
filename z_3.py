import cv2

image = cv2.imread("./assets/bird.jpg")
cv2.imshow("img", image)
(h, w) = image.shape[:2]


(b, g, r) = image[h//2, w//2]
print("Pixel at (h/2, w/2) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.waitKey(0)
cv2.destroyAllWindows()
