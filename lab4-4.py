# 61011212027

import cv2
import numpy as np


# Non-maximum suppression
def non_max_suppression(magnitude, angle):
    # getting the dimensions of the input image
    height, width = magnitude.shape
    out = np.zeros(magnitude.shape)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            direction = angle[row, col]

            # (0 degree)
            if (0 <= direction < 22.5) or (337.5 <= direction <= 360):
                before_pixel = magnitude[row, col - 1]
                after_pixel = magnitude[row, col + 1]
            # (45 degree)
            elif (22.5 <= direction < 67.5) or (180 <= direction < 247.5):
                before_pixel = magnitude[row + 1, col - 1]
                after_pixel = magnitude[row - 1, col + 1]
            # (90 degree)
            elif (67.5 <= direction < 112.5) or (247.5 <= direction < 292.5):
                before_pixel = magnitude[row - 1, col]
                after_pixel = magnitude[row + 1, col]
            # (135 degree)
            else:
                before_pixel = magnitude[row - 1, col - 1]
                after_pixel = magnitude[row + 1, col + 1]

            if magnitude[row, col] >= before_pixel and \
                    magnitude[row, col] >= after_pixel:
                out[row, col] = magnitude[row, col]
    return out


# double thresholding step
def double_threshold(mag, weak_th, strong_th):
    height, width = mag.shape
    weak, strong = 25, 255
    for i in range(height):
        for j in range(width):
            grad_mag = mag[i, j]
            if grad_mag < weak_th:
                mag[i, j] = 0
            elif strong_th > grad_mag >= weak_th:
                mag[i, j] = weak
            else:
                mag[i, j] = strong
        return mag, weak


# Hysteresis step
def hysteresis(img, weak, strong=255):
    M, N = img.shape
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            if img[i, j] == weak:
                if (img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) \
                        or (img[i + 1, j + 1] == strong) or (img[i, j - 1] == strong) \
                        or (img[i, j + 1] == strong) or (img[i - 1, j - 1] == strong) \
                        or (img[i - 1, j] == strong) or (img[i - 1, j + 1] == strong):
                    img[i, j] = strong
                else:
                    img[i, j] = 0
    return img


def Canny_detector(img, weak_th=None, strong_th=None):
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img3 = cv2.GaussianBlur(img2, (5, 5), 1.4)

    gx = cv2.Sobel(np.float32(img3), cv2.CV_64F, 1, 0, 3)
    gy = cv2.Sobel(np.float32(img3), cv2.CV_64F, 0, 1, 3)

    magnitude, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)

    mag_max = np.max(magnitude)
    if not weak_th:
        weak_th = mag_max * 0.1
    if not strong_th:
        strong_th = mag_max * 0.5

    mag = non_max_suppression(magnitude, angle)
    mag_thr, weak = double_threshold(mag, weak_th, strong_th)
    out = hysteresis(mag_thr, weak)
    return out


def funCan(src, thr=0):
    thr1 = 100
    thr2 = 1
    edge = cv2.Canny(src, thr1, thr2)
    return edge


img1 = cv2.imread('4.jpg')

img_canny1 = Canny_detector(img1, 100, 40)

imgGB = cv2.GaussianBlur(img1, (5, 5), 1.4)
img_canny2 = funCan(imgGB)

cv2.imshow('original', img1)
cv2.imshow('canny with out cv2 func', img_canny1)
cv2.imshow('canny with cv2 func', img_canny2)
cv2.waitKey()
