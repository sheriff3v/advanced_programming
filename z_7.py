import cv2

image = cv2.imread("./assets/bird.jpg")
cv2.imshow("before",image)
(h, w) = image.shape[:2]
(cX, cY) = (w //3, h // 3)

center = image[cY:cY +cY, cX:cX+cX]
cv2.imshow("after",center)

cv2.waitKey(0)
cv2.destroyAllWindows()



