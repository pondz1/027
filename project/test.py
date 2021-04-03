
import cv2
import numpy as np




def remove_shadow(img_rgb):
    rgb_planes = cv2.split(img_rgb)
    result_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7, 7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        result_planes.append(diff_img)
        cv2.namedWindow('dilated_img', cv2.WINDOW_NORMAL)
        cv2.imshow('dilated_img', dilated_img)
        cv2.namedWindow('bg_img', cv2.WINDOW_NORMAL)
        cv2.imshow('bg_img', bg_img)
    return cv2.merge(result_planes)


img = cv2.imread('1.jpg')
result = remove_shadow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
result2 = remove_shadow(img)
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
_, thres = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
_, thres2 = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.namedWindow('aa', cv2.WINDOW_NORMAL)
cv2.imshow('aa', thres)
cv2.namedWindow('bb', cv2.WINDOW_NORMAL)
cv2.imshow('bb', thres2)
cv2.waitKey(0)
cv2.destroyAllWindows()
