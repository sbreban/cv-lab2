import sys

import cv2 as cv
import numpy as np

try:
    fn = sys.argv[1]
except:
    fn = 'contour.jpg'

img = cv.imread(fn, True)
if img is None:
    print('Failed to load image file:', fn)
    sys.exit(1)

h, w = img.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)
seed_pt = None
fixed_range = True
connectivity = 4


def update(dummy=None):
    if seed_pt is None:
        cv.imshow('floodfill', img)
        return
    flooded = img.copy()
    mask[:] = 0
    flags = connectivity
    if fixed_range:
        flags |= cv.FLOODFILL_FIXED_RANGE
    cv.floodFill(flooded, mask, seed_pt, (0, 0, 255), (20,) * 3, (20,) * 3, flags)
    cv.circle(flooded, seed_pt, 2, (0, 0, 255), -1)
    cv.imshow('floodfill', flooded)


def onmouse(event, x, y, flags, param):
    global seed_pt
    if flags & cv.EVENT_FLAG_LBUTTON:
        seed_pt = x, y
        update()


update()
cv.setMouseCallback('floodfill', onmouse)

while True:
    ch = cv.waitKey()
    if ch == 27:
        break

cv.destroyAllWindows()
