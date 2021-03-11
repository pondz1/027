import cv2
import numpy as np
img = np.zeros((9, 11), np.uint8)
img[1:5, 2] = 1
img[2, 5:9] = 1
img[3, 1:4] = 1
img[5:8, 4] = 1
img[6, 3:6] = 1
img[4:6, 7:9] = 1
img[5, 9] = img[6, 8] = 1
print(img)
bg = np.where(img > 0.5, 0, 1).astype(np.uint8)
print(bg)
B1 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
B2 = np.array([[1, 0, 1], [0, 0, 0], [1, 0, 1]], np.uint8)
dst_erode1 = cv2.erode(img, B1, iterations=1)
print(dst_erode1)
dst_erode2 = cv2 .erode(bg, B2, iterations=1)
print(dst_erode2)
out = cv2.bitwise_and (dst_erode1, dst_erode2)
print(out)
h, w = img. shape[0]*20, img. shape[1]*20
cv2.imshow('Original', cv2.resize(img, (h, w),
                                  interpolation=cv2. INTER_AREA)*255)
cv2 . imshow('Erosion1', cv2.resize(dst_erode1, (h, w),
                                    interpolation=cv2.INTER_AREA)*255)
cv2 . imshow(' Erosion2', cv2.resize(dst_erode2, (h, w),
                                     interpolation=cv2.INTER_AREA)*255)
cv2. imshow('Hit or Miss', cv2 .resize(out, (h, w),
                                       interpolation=cv2.INTER_AREA)*255)

cv2.waitKey()
cv2.destroyAllWindows()
