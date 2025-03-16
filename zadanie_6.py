import cv2

image = cv2.imread("assets/img.png")

print("Wybierz sposób odbicia:")
print("0 - Odbicie pionowe")
print("1 - Odbicie poziome")
print("-1 - Odbicie zarówno w pionie, jak i w poziomie")

flip_type = int(input("Podaj numer odbicia: "))

if flip_type == 0:
    flipped_image = cv2.flip(image, 0)
elif flip_type == 1:
    flipped_image = cv2.flip(image, 1)
elif flip_type == -1:
    flipped_image = cv2.flip(image, -1)
else:
    print("Niepoprawny wybór!")
    exit()

cv2.imshow("Original Image", image)
cv2.imshow("Flipped Image", flipped_image)

cv2.waitKey(0)

