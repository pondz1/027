import cv2
path = "../misc/house.tiff"
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
size = 11
blurred = cv2.GaussianBlur(img, (size, size), cv2.BORDER_DEFAULT)
g_hpf = cv2.subtract(img,blurred)
cv2.imshow('high pass filter', g_hpf)
cv2.imshow('original', img)
cv2.waitKey()
cv2.destroyAllWindows()

