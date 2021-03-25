# otsu.py - Simple (and non-efficient) implementation of Otsu's method
#
# You can do with this code whatever you want. The main purpose is help
# people learning about this. Also, there is no warranty of any kind.
#
# Juan Miguel Valverde Martinez
# http://laid.delanover.com

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Image4Otsu/sudoku.png', 0)
blur = cv2.GaussianBlur(img, (5, 5), 0)
# find normalized_histogram, and its cumulative distribution function
hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
hist_norm = hist.ravel() / hist.sum()
print(sum(hist_norm))
Q = hist_norm.cumsum()
bins = np.arange(256)
fn_min = np.inf
thresh = -1
for i in range(1, 256):
    p1, p2 = np.hsplit(hist_norm, [i])  # probabilities
    q1, q2 = Q[i], Q[255] - Q[i]  # cum sum of classes
    if q1 < 1.e-6 or q2 < 1.e-6:
        continue
    b1, b2 = np.hsplit(bins, [i])  # weights
    # finding means and variances
    m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
    v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2
    # calculates the minimization function
    fn = v1 * q1 + v2 * q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

print("Threshold: {}".format(thresh))

plt.subplot(121)
plt.imshow(img, cmap='gray')
# plt.subplot(142)
# plt.hist(im_flat, bins=256, range=(0, 255))
plt.subplot(122)
plt.imshow(blur > thresh, cmap='gray')
plt.show()
