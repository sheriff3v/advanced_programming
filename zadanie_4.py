import cv2
image = cv2.imread("assets/img.png")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w * 3, h * 3)
resizedNearest = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_NEAREST)
resizedLinear = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_LINEAR)
resizedCubic = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_CUBIC)
resizedLanczo = cv2.resize(image, (cX, cY), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Resized Nearest", resizedNearest)
cv2.imshow("Resized Linear", resizedLinear)
cv2.imshow("Resized Cubic", resizedCubic)
cv2.imshow("Resized Lanczo", resizedLanczo)
cv2.waitKey(0)