import cv2

image = cv2.imread("assets/cat.jpg")
(h, w, c) = image.shape[:3]
print(f'channels: {c}')