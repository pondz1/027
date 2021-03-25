import numpy as np
import cv2
import matplotlib.pyplot as plt

# Open the image
file = './project/1.jpg'
img = cv2.imread(file, 0)
h, w = img.shape
thr = 127

# define images with 0s

# Gradient
Gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
Gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Edge Magnitude
Gxy = np.sqrt(Gx ** 2 + Gy ** 2)

# Check grandient with threshold
G = np.array([[255 if g > thr else 0 for g in Gxy[j]] for j in range(h)], dtype=np.uint8)

plt.figure(2, figsize=(12, 7))
plt.subplot(231)
plt.title(file + ' 2'), plt.axis('off')
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
