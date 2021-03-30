import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('4.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hight,width = gray.shape
print(gray.shape)
# print(hight/2.5)
# print(width/2.5)
# edges = cv2.Canny(gray, 200, 250)
ret, thres = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

contours, hierarchy = cv2.findContours(
    thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
border = []
max_list = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    max_list.append(area)

max_list.sort()
MAXS = max_list[len(max_list)-4]
print("maxs = " + str(MAXS))
for i,cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    if area < MAXS:
        continue
    print(area)
    cnt_len = cv2.arcLength(cnt, True)
    orig_cnt = cnt.copy()
    cnt = cv2.approxPolyDP(cnt, 0.01 * cnt_len, True)
    x,y,w,h = cv2.boundingRect(orig_cnt)
    if y > hight/1.9:
        border.append([x, y, w, h])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# cv2.drawContours(imgrgb, contours, -1, (0, 255, 0), 3)
row = int(len(border))
col = row
print(row)
# for i,value in enumerate(border):
#     x, y, w, h = value
#     plt.subplot(row, col, i+1)
#     plt.imshow(imgrgb[y:y+h,x:x+w], 'gray')
#     plt.title(value)
#     plt.xticks([]), plt.yticks([])

# # # plt.imshow(edges > 0, cmap='gray')
# plt.show()

# # (B, G, R) = cv2.split(img)
# zero_ch = np.zeros(R.shape, np.uint8)
# r = np.where(R > 200, 255, 0)
# print(R)
# print(r[0,0])
# red = cv2.merge([B, G, R])
# print(r.shape)
# cv2.imshow('Mouth Detector', edges[460:600, 600:800])
# x, y, w, h = border[6]
# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# for xx in border:
#     cv2.namedWindow('Mouth Detector', cv2.WINDOW_NORMAL)
#     cv2.imshow('Mouth Detector', img[xx[1]:xx[1]+xx[3], xx[0]:xx[0]+xx[2]])
#     cv2.waitKey(0)
#     print(xx)
#     cv2.destroyAllWindows()

cv2.namedWindow('Mouth Detector', cv2.WINDOW_NORMAL)
cv2.imshow('Mouth Detector', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# x, y, w, h
# print(len(border))
