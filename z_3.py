import cv2

image = cv2.imread("./assets/cat.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("test", image)

is_gray = image.shape
if len(is_gray) == 2:
    print("image is grey and has 1 channel")
else:
    print(is_gray[2])

cv2.waitKey(0)
cv2.destroyAllWindows()
