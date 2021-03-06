import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 7), constrained_layout=True)
img_c1 = cv2.imread('misc/s047.tif', 0)
img_c2 = np.fft.fft2(img_c1)  # 2D FFT
img_c3 = np.fft.fftshift(img_c2)  # FFT SHIFT
img_c4 = np.fft.ifftshift(img_c3)  # Inverse FFT SHIFT
img_c5 = np.fft.ifft2(img_c4)  # Inverse 2D FFT
img_c6 = np.angle(img_c2)  # Phase Spectrum

fs = np.log(1 + np.abs(img_c2))
cs = np.log(1 + np.abs(img_c3))
d = np.log(1 + np.abs(img_c4))
pi = np.abs(img_c5)

plt.subplot(231), plt.imshow(img_c1, 'gray')
plt.title('Original Image'), plt.axis('off')
plt.subplot(232), plt.imshow(fs, 'gray')
plt.title('Frequency Spectrum'), plt.axis('off')
plt.subplot(233), plt.imshow(img_c6, 'gray')
plt.title('Phase Spectrum'), plt.axis('off')
plt.subplot(234), plt.imshow(cs, 'gray')
plt.title('Centered Spectrum'), plt.axis('off')
plt.subplot(235), plt.imshow(d, 'gray')
plt.title('Decentralized'), plt.axis('off')
plt.subplot(236), plt.imshow(pi, 'gray')
plt.title('Processed Image'), plt.axis('off')
plt.show()
