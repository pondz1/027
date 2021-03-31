import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg')

imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rgb_planes = cv2.split(imgrgb)
result_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((3, 3), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img = cv2.normalize(
        diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)

result = cv2.merge(result_planes)
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
hight, width = gray.shape
edges = cv2.Canny(gray, 200, 250)
ret, thres = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)




contours, hierarchy = cv2.findContours(
    thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
border = []
max_list = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    max_list.append(area)

max_list.sort()
print(len(max_list))
per = int(len(max_list)*0.35/100)
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
    if y > hight/2 and w>h:
        border.append([x, y, w, h])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.namedWindow('Mouth Detector', cv2.WINDOW_NORMAL)
cv2.imshow('Mouth Detector', img)
# cv2.namedWindow('thr', cv2.WINDOW_NORMAL)
# cv2.imshow('thr', thres)
cv2.waitKey(0)
cv2.destroyAllWindows()

