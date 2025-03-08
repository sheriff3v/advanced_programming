import cv2

image = cv2.imread("./assets/bird.jpg")
cv2.imshow("img", image)
(h, w) = image.shape[:2]


(b, g, r) = image[50, 50]
(b2, g2, r2) = image[100, 100]
print("Diff - Red: {}, Green: {}, Blue: {}".format(abs(r-r2), abs(g-g2), abs(b-b2)))

cv2.waitKey(0)
cv2.destroyAllWindows()
