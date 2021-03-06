# 61011212027
import cv2
import numpy as np


filename = 'misc/s047.tif'
img = cv2.imread(filename, 0)
cv2.namedWindow('Grayscale', cv2.WINDOW_NORMAL)
cv2.imshow('Grayscale', img)

mask1 = np.ones(img.shape, dtype=np.uint8) * 64

out = cv2.subtract(img, mask1)
cv2.namedWindow('Subtract', cv2.WINDOW_NORMAL)
cv2.imshow('Subtract', out)

cv2.waitKey(0)
cv2.destroyAllWindows()