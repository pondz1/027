import cv2

path = "../misc/house.tiff"
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
size = 5
dst = cv2.GaussianBlur(img, (size, size), cv2.BORDER_DEFAULT)
cv2.imshow('low pass filter', dst)
cv2.imshow('original', img)
cv2.waitKey()
cv2.destroyAllWindows()
