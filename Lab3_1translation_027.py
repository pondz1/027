# 61011212027
import cv2
import numpy as np


def translation(src, shift, shape_out):
    h, w = src.shape[:2]
    out_img = np.zeros(shape_out, dtype=np.uint8)

    for i in range(shift[1], h):
        for j in range(shift[0], w):
            out_img[i, j] = src[i - shift[1], j - shift[0]]
    return out_img


image = cv2.imread('misc/house.tiff')
height, width = image.shape[:2]
shift = (100, 100)
img_trans = translation(image, shift, image.shape)
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', image)
cv2.namedWindow('translation', cv2.WINDOW_NORMAL)
cv2.imshow('translation', img_trans)

cv2.waitKey(0)
cv2.destroyAllWindows()
