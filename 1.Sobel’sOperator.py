import numpy as np
import cv2
import matplotlib.pyplot as plt

# Open the image
file = './misc/house.tiff'
img = cv2.imread(file, 0)
h, w = img.shape
thr = 127

hx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
hy = hx.T

Gx = np.zeros((h, w))
Gy = np.zeros((h, w))
Gxy = np.zeros((h, w))
G = np.zeros((h, w))
theta = np.zeros((h, w))
for i in range(1, h - 1):
    for j in range(1, h - 1):
        # Gradient
        Gx.itemset((i, j), np.sum(hx * img[i - 1:i + 2, j - 1:j + 2]))
        Gy.itemset((i, j), np.sum(hy * img[i - 1:i + 2, j - 1:j + 2]))

        # Edge Magnitude
        Gxy.itemset((i, j), np.sqrt(Gx[i, j] ** 2 + Gy[i, j] ** 2.0))

        # Check grandient with threshold
        if Gxy.item(i, j) > thr:
            G.itemset((i, j), 255)
        else:
            G.itemset((i, j), 0)

plt.figure(2, figsize=(12, 7))
plt.subplot(231)
plt.title(file), plt.axis('off')
plt.imshow(img, cmap='gray')

plt.subplot(232)
plt.title('Sobel Gx'), plt.axis('off')
plt.imshow(Gx, cmap='gray')

plt.subplot(233)
plt.title('Sobel Gy'), plt.axis('off')
plt.imshow(Gy, cmap='gray')

plt.subplot(234)
plt.title('Sobel Gradient'), plt.axis('off')
plt.imshow(Gxy, cmap='gray')

plt.subplot(235)
plt.title('Edge'), plt.axis('off')
plt.imshow(G, cmap='gray')

plt.imsave('house-Sobel-1.png', Gxy, cmap='gray')
plt.show()
