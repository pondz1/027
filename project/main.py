import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('7.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hight, width = gray.shape
edges = cv2.Canny(gray, 200, 250)
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
print(len(max_list))
per = int(len(max_list)*0.40/100)+4
print(per)
MAXS = max_list[len(max_list)-per]
print("maxs = " + str(MAXS))
for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    if area < MAXS:
        continue
    print(area)
    cnt_len = cv2.arcLength(cnt, True)
    orig_cnt = cnt.copy()
    cnt = cv2.approxPolyDP(cnt, 0.01 * cnt_len, True)
    x, y, w, h = cv2.boundingRect(orig_cnt)
    if y > hight/1.9:
        border.append([x, y, w, h])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.namedWindow('Mouth Detector', cv2.WINDOW_NORMAL)
cv2.imshow('Mouth Detector', thres)
cv2.waitKey(0)
cv2.destroyAllWindows()

