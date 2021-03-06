# 61011212027

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

src = cv.imread('misc/house.tiff', 0)

gb = cv.GaussianBlur(src, (5, 5), cv.BORDER_DEFAULT)
# Gradient
Gx = cv.Sobel(src, cv.CV_64F, 1, 0, ksize=3)
Gy = cv.Sobel(src, cv.CV_64F, 0, 1, ksize=3)
# Edge Magnitude
Gxy = np.sqrt(Gx ** 2 + Gy ** 2)

Gx2 = cv.Sobel(gb, cv.CV_64F, 1, 0, ksize=3)
Gy2 = cv.Sobel(gb, cv.CV_64F, 0, 1, ksize=3)
# Edge Magnitude
Gxy2 = np.sqrt(Gx2 ** 2 + Gy2 ** 2)

plt.subplot(221)
plt.title('house'), plt.axis('off')
plt.imshow(src, cmap='gray')

plt.subplot(222)
plt.title('Gaussian filter'), plt.axis('off')
plt.imshow(gb, cmap='gray')


plt.subplot(223)
plt.title('With out Gaussian filter'), plt.axis('off')
plt.imshow(Gxy, cmap='gray')

plt.subplot(224)
plt.title('with Gaussian filter'), plt.axis('off')
plt.imshow(Gxy2, cmap='gray')




plt.show()
