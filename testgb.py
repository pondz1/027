import cv2 as cv
import matplotlib.pyplot as plt

src = cv.imread('./imgtest/WIN.jpg')

gb = cv.medianBlur(src,21)

# plt.subplot(222)
plt.title('with Gaussian filter'), plt.axis('off')
plt.imshow(gb, cmap='gray')

plt.show()