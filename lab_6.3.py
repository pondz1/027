# 61011212027
import cv2
import numpy as np
from matplotlib import pyplot as plt


def dilate_and_erode(img, kernel):

    dilate = cv2.dilate(img, kernel, iterations=1)
    erode = cv2.erode(img, kernel, iterations=1)
    return dilate, erode


def opening(img, kernel):
    erode = cv2.erode(img, kernel, iterations=1)
    dilate = cv2.dilate(erode, kernel, iterations=1)
    return dilate


def closing(img, kernel):
    dilate = cv2.dilate(img, kernel, iterations=1)
    erode = cv2.erode(dilate, kernel, iterations=1)
    return erode


img = cv2.imread('./Image4Otsu/sudoku.png', 0)
kernel = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]], np.uint8)

dst_dilate, dst_erode = dilate_and_erode(img, kernel)
dst_open = opening(img, kernel)
dst_close = closing(img, kernel)

titles = ['Dilation', 'Erosion', 'Opening', 'Closing']
images = [dst_dilate, dst_erode, dst_open, dst_close]
for i in range(len(images)):
    plt.subplot(len(images)/2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
