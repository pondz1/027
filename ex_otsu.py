# 61011212027

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./misc/house.tiff', 0)
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 150, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 150, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 150, 255, cv.THRESH_TOZERO_INV)
ret, thresh6 = cv.threshold(img, 0, 255, cv.THRESH_OTSU)

ret, thresh7 = cv.threshold(img, 0, 255, cv.THRESH_TOZERO + cv.THRESH_OTSU)

titles = ['Original Image', 'BINARY',
          'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV', 'OTSU', 'TOZERO + OTSU']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7]
for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
