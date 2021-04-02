import cv2
import numpy as np
from matplotlib import pyplot as plt


def remove_shadow(img_rgb):
    rgb_planes = cv2.split(img_rgb)
    result_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        result_planes.append(diff_img)
    return cv2.merge(result_planes)


def find_max_list(contour):
    max_list = []
    for cnt in contour:
        area = cv2.contourArea(cnt)
        max_list.append(area)

    max_list.sort()
    per = int(len(max_list)*1/100)
    max_c = max_list[len(max_list)-per]
    return max_c

if __name__ == '__main__':

    img = cv2.imread('1.jpg')
    result = remove_shadow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _, thres = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    MAXS = find_max_list(contours)
    HEIGT, WIDTH = gray.shape

    max_rec = 0
    box_rec = None

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < MAXS:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        if y > HEIGT/2 and w > h and (w+h) >= max_rec \
                and (x >= WIDTH/3) and (x <= WIDTH - WIDTH/3):
            max_rec = (w+h)
            box_rec = [x,y,w,h]
                
    x, y, w, h = box_rec
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.namedWindow('max rectangle', cv2.WINDOW_NORMAL)
    cv2.imshow('max rectangle', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# and (w+h) >= max_rec
