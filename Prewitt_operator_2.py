import numpy as np
import cv2
import matplotlib.pyplot as plt

# Open the image
file = './misc/house.tiff'
img = cv2.imread(file, 0)
h, w = img.shape
thr = 127

# define images with 0s
Gxy = np.zeros((h, w), dtype=np.float64)
g = np.zeros((h, w), dtype=np.uint8)
theta = np.zeros((h, w))

# Gradient
hx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
hy = hx.T
Gx = cv2.filter2D(img, cv2.CV_64F, hx)
Gy = cv2.filter2D(img, cv2.CV_64F, hy)

# Edge Magnitude
Gxy = np.sqrt(Gx ** 2 + Gy ** 2)

# direction
theta = np.arctan2(Gy, Gx) * (180 / np.pi) % 180

# Check grandient with threshold
G = np.array([[255 if g > thr else 0 for g in Gxy[j]] for j in range(h)], dtype=np.uint8)

plt.figure(2, figsize=(12, 7))
plt.subplot(231)
plt.title(file + ' 2'), plt.axis('off')
plt.imshow(img, cmap='gray')

plt.subplot(232)
plt.title('Prewitt Gx'), plt.axis('off')
plt.imshow(Gx, cmap='gray')

plt.subplot(233)
plt.title('Prewitt Gy'), plt.axis('off')
plt.imshow(Gy, cmap='gray')

plt.subplot(234)
plt.title('Prewitt Gradient'), plt.axis('off')
plt.imshow(Gxy, cmap='gray')

plt.subplot(235)
plt.title('Edge'), plt.axis('off')
plt.imshow(G, cmap='gray')

plt.imsave('house-prewitt-1.png', Gxy, cmap='gray')
plt.show()
