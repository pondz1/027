import numpy as np
import cv2

filename = './misc/opencv-1ogo.png'
img = cv2.imread(filename)
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.imshow('Original', img)
# แยก channel
channel = cv2.split(img)
ch = ['B', 'G', ' R']
for i, plane in enumerate(channel):
    cv2.namedWindow(' Channel [%s] '%ch[i], cv2.WINDOW_NORMAL)
    cv2. imshow('Channel [%s]'%ch[i], plane)
# สร้าง Plane ด้วมค่า 0
zero_ch = np.zeros(channel[0].shape, np.uint8)
# รวม channe1 (นทีนี่แยกให้เห็น 3 ภาพสี 3 channel
merge_ch = []
merge_ch.append(cv2.merge([channel[0], zero_ch, zero_ch]))
merge_ch.append(cv2.merge([zero_ch, channel[1], zero_ch]))
merge_ch.append(cv2.merge([zero_ch, zero_ch, channel[2]]))
for i, plane in enumerate(merge_ch):
    cv2.namedWindow('Merge Channel [%s] ' % ch[i], cv2.WINDOW_NORMAL)
    cv2.imshow('Merge Channel [%s]' % ch[i], plane)
cv2.waitKey()
cv2.destroyAllWindows()
