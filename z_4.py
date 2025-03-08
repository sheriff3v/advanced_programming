import cv2

image = cv2.imread("./assets/bird.jpg")

x = int(input("Write x: "))
y = int(input("Write y: "))

(h, w) = image.shape[:2]
if x > w or x < 0:
    print("Wrong param for x")
elif y > h or y < 0:
    print("Wrong param for y ")

image[y, x] = (0, 0, 0)


cv2.imshow("after", image)



(b, g, r) = image[y, x]
print("Pixel at x, y  - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.waitKey(0)
cv2.destroyAllWindows()
