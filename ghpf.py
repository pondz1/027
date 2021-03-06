import cv2


def high_pass(image, size):
    blurred = cv2.GaussianBlur(image, (size, size), cv2.BORDER_DEFAULT)
    g_hpf = cv2.subtract(img, blurred)
    return g_hpf


def low_pass(image, size):
    dst = cv2.GaussianBlur(image, (size, size), cv2.BORDER_DEFAULT)
    return dst


path = "./misc/house.tiff"
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
hp = high_pass(img, 11)
lp = low_pass(img, 11)

cv2.imshow('original', img)
cv2.imshow('high pass filter', hp)
cv2.imshow('low pass filter', lp)
cv2.waitKey()
cv2.destroyAllWindows()
