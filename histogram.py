import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram(img, L=256):
    h = np.zeros(L, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            h[img.item(i, j)] += 1
    return h


def equalization(img):
    L = 256
    p, bins = np.histogram(img, bins=L, range=(0,L))
    p = p/img.size
    P = p.copy()
    out = np.zeros(img.shape, dtype=np.uint8)

    for j in range(1,L):
        P[j] = P[j-1] + P[j]
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            a = int(P[img.item(i, j)]*(L-1))
            out.itemset((i, j), a)
    plt.show()
    return out.astype(np.uint8), P


filename = 'misc/house.tiff'
img = cv2.imread(filename, 0)
cv2.namedWindow('Grayscale', cv2.WINDOW_NORMAL)
cv2.imshow('Grayscale', img)

img_eq_in = equalization(img)

img_eq = equalization(img)
cv2.namedWindow('Image Equalization', cv2.WINDOW_NORMAL)
cv2.imshow('Image Equalization', img_eq[0])

his_in = histogram(img_eq_in[0])
his = histogram(img_eq[0])
print(img_eq[0].shape)

plt.plot(his[1])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()