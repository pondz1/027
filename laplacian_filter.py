#61011212027
import cv2
import numpy as np


def laplacian_filter(file_name):
    mask = np.array([[0, 0, -1, 0, 0],
                     [0, -1, -2, -1, 0],
                     [-1, -2, 16, -2, -1],
                     [0, -1, -2, -1, 0],
                     [0, 0, -1, 0, 0]])
    image = cv2.imread(file_name, 0)
    width, height = image.shape
    out = np.zeros(image.shape, dtype=np.uint8)
    for i in range(2, height-3):
        for j in range(2, width-3):
            laplacian = image[i-2:i+3, j-2:j+3]
            s = (mask*laplacian).sum()
            if s < 0:
                s = 0
            if s > 255:
                s = 255

            out.itemset((i, j), s)
    cv2.imshow('house', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


filename = 'misc/house.tiff'
laplacian_filter(filename)
