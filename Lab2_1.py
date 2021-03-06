import cv2
import numpy as np


def median_filter(filename, size):
    image = cv2.imread(filename, 0)
    width, height = image.shape
    s1 = round(size / 2)
    s2 = size - s1
    print(s1 + s2)
    out = np.zeros(image.shape, dtype=np.uint8)
    for i in range(s1, height - s1):
        for j in range(s1, width - s1):
            out.itemset((i, j), np.median(image[i - s1:i + s2, j - s1:j + s2]))
    cv2.imshow('airplane', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


filename = 'airplane_sp.png'
median_filter(filename, 3)
median_filter(filename, 5)
median_filter(filename, 7)
median_filter(filename, 9)
