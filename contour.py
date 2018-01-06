import cv2
import numpy as np

img = cv2.imread('k.jpg', 0)
cross = np.array([
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]], dtype=np.uint8)
diamond = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]], dtype=np.uint8)
r1 = cv2.erode(img, cross, iterations=1)
r1 = cv2.dilate(r1, diamond, iterations=1)

xshape = np.array([
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]], dtype=np.uint8)
square = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]], dtype=np.uint8)
r2 = cv2.erode(img, xshape, iterations=1)
r2 = cv2.dilate(r2, square, iterations=1)
r = cv2.absdiff(r2, r1)
cv2.imshow('image', r)
k = cv2.waitKey(0) & 0xFF
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
