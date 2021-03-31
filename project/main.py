import cv2
import numpy as np
from matplotlib import pyplot as plt
import random as rng


def remove_shadow(img_rgb):
    rgb_planes = cv2.split(img_rgb)
    result_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        result_planes.append(diff_img)
    return cv2.merge(result_planes)


def find_max_ellps(contour,max_list,hight):
    max_ellps = 0
    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area < max_list:
            continue
        if cnt.shape[0] > 5:
            elps = cv2.fitEllipse(cnt)
            x, y, w, h = cv2.boundingRect(cnt)
            if y > hight/2 and w > h and elps[1][0] > max_ellps and (elps[0][1] > 0 and elps[0][0] > 0):
                max_ellps = elps[1][0]
    return max_ellps


def find_max_list(contour):
    max_list = []
    for cnt in contour:
        area = cv2.contourArea(cnt)
        max_list.append(area)

    max_list.sort()
    per = int(len(max_list)*1/100)
    max_c = max_list[len(max_list)-per]
    return max_c

img = cv2.imread('1.jpg')
imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result = remove_shadow(imgrgb)
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
HEIGT, _ = gray.shape
_ , thres = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours, _ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(img, contours, -1, (0, 255, 0), 3)


MAXS = find_max_list(contours)

max_ellps = find_max_ellps(contours,MAXS,HEIGT)
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < MAXS:
        continue
    if cnt.shape[0] > 5:
        elps = cv2.fitEllipse(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        if y > HEIGT/2 and w > h and elps[1][0] == max_ellps:
            print(elps)
            print(cv2.boundingRect(cnt))
            cv2.ellipse(img, elps, (0, 0, 255), 2)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.namedWindow('Mouth Detector', cv2.WINDOW_NORMAL)
cv2.imshow('Mouth Detector', img)
cv2.namedWindow('thr', cv2.WINDOW_NORMAL)
cv2.imshow('thr', thres)
cv2.waitKey(0)
cv2.destroyAllWindows()
