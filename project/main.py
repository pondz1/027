import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 200)
# print(edges > 0)
# (B, G, R) = cv2.split(img)
# zero_ch = np.zeros(R.shape, np.uint8)
# r = np.where(R > 200, 255, 0)
# print(R)
# print(r[0,0])
# red = cv2.merge([B, G, R])
# print(r.shape)
# cv2.imshow('Mouth Detector', edges[460:600, 600:800])
cv2.namedWindow('Mouth Detector', cv2.WINDOW_NORMAL)
cv2.imshow('Mouth Detector', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(edges > 0, cmap='gray')
# plt.show()

