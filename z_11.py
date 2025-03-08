import cv2
import numpy as np

image = cv2.imread('assets/bird.jpg')

if image is None:
    print("Nie udało się wczytać obrazu.")
    exit()

max_brightness = -1
max_brightness_pixel = None

height, width, _ = image.shape

for y in range(height):
    for x in range(width):
        b, g, r = image[y, x]

        brightness = (b + g + r) / 3

        if brightness > max_brightness:
            max_brightness = brightness
            max_brightness_pixel = (x, y)

if max_brightness_pixel:
    print(f"Najjaśniejszy piksel znajduje się w miejscu {max_brightness_pixel} o jasności {max_brightness}")
else:
    print("Brak piksela w obrazie.")
