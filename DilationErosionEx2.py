import cv2
import numpy as np
from matplotlib import pyplot as plt


def dilate_and_erode(img, kernel):
    thr, bin_img = cv2.threshold(
        img, 0, 1, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    dilate = cv2.dilate(bin_img, kernel, iterations=1)
    erode = cv2.erode(bin_img, kernel, iterations=1)

    return dilate, erode, bin_img


def opening(img, kernel):
    thr, bin_img = cv2.threshold(
        img, 0, 1, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    erode = cv2.erode(bin_img, kernel, iterations=1)
    dilate = cv2.dilate(erode, kernel, iterations=1)
    return dilate


def closing(img, kernel):
    thr, bin_img = cv2.threshold(
        img, 0, 1, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    dilate = cv2.dilate(bin_img, kernel, iterations=1)
    erode = cv2.erode(dilate, kernel, iterations=1)
    return erode


img = cv2.imread('./DilationErosionImage/text-line.jpg', 0)
# kernel = np.ones((3, 3), np.uint8)
kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)

dst_dilate, dst_erode, bin_img = dilate_and_erode(img, kernel)
dst_open = opening(img, kernel)
dst_close = closing(img, kernel)

titles = ['BINARY', 'Dilation', 'Erosion', 'Opening', 'Closing']
images = [bin_img, dst_dilate, dst_erode, dst_open, dst_close]
for i in range(len(images)):
    plt.subplot(len(images), 1, i+1)
    plt.imshow(images[i]*255, 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
