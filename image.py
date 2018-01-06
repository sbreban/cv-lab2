import cv2
import numpy as np

watermark = cv2.imread('cyclist.png', cv2.IMREAD_UNCHANGED)
(wH, wW) = watermark.shape[:2]
# (B, G, R, A) = cv2.split(watermark)
# B = cv2.bitwise_and(B, B, mask=A)
# G = cv2.bitwise_and(G, G, mask=A)
# R = cv2.bitwise_and(R, R, mask=A)
# watermark = cv2.merge([B, G, R, A])

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
overlay = np.zeros((h, w, 4), dtype="uint8")
overlay[h - wH - 10:h - 10, w - wW - 10:w - 10] = watermark
output = image.copy()
cv2.addWeighted(overlay, 1.0, output, 1.0, 0, output)
cv2.imshow('image', output)
k = cv2.waitKey(0) & 0xFF
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('image_watermarked.png', image)
    cv2.destroyAllWindows()
