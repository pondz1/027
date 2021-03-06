# 61011212027

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Scan0024.TIF', 0)
blur = cv2.GaussianBlur(img, (3, 3), 0)

hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
hist = hist.ravel() / hist.sum()

K = np.arange(256)
sum_P = hist.cumsum()

fn_min = np.inf
thresh = -1

for i in range(1, 256):
    p1, p2 = np.hsplit(hist, [i])
    k1, k2 = np.hsplit(K, [i])
    sum_P1 = sum_P[i]
    sum_P2 = sum_P[255] - sum_P[i]

    m1 = np.sum(p1 * k1) / sum_P1
    m2 = np.sum(p2 * k2) / sum_P2
    v1 = np.sum(((k1 - m1) ** 2) * p1) / sum_P1
    v2 = np.sum(((k2 - m2) ** 2) * p2) / sum_P2

    fn = v1 * sum_P1 + v2 * sum_P2
    # fn = sum_P1 * sum_P2 * ((m2-m1)**2) / np.sum(((k1 - np.sum(p2 * k2)) ** 2) * p1)
    if fn < fn_min:
        fn_min = fn
        thresh = i

print("Threshold: {}".format(thresh))

plt.subplot(121)
plt.imshow(img, cmap='gray')

plt.subplot(122)
plt.imshow(blur > thresh, cmap='gray')

plt.show()
