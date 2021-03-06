import cv2

file = './Image4Otsu/sudoku.png'
img = cv2.imread(file, 0)
dst1 = cv2.ximgproc.niBlackThreshold(img, 255, cv2.THRESH_BINARY,
                                     65, -0.2, cv2.ximgproc.BINARIZATION_NIBLACK)
dst2 = cv2.ximgproc.niBlackThreshold(img, 255, cv2.THRESH_BINARY,
                                     65, -0.2, cv2.ximgproc.BINARIZATION_SAUVOLA)

dst3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 11, 2)
dst4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 11, 2)


cv2.imshow('Original', cv2.resize(img, (256, 256)))
cv2.imshow('Niblack', cv2.resize(dst1, (256, 256)))
cv2.imshow('Sauvola', cv2.resize(dst2, (256, 256)))
cv2.imshow('Mean C', cv2.resize(dst3, (256, 256)))
cv2.imshow('Gaussian C', cv2.resize(dst4, (256, 256)))

cv2.waitKey(0)
