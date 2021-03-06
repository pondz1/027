from PIL import Image
import cv2
import numpy as np

filename = 'myCats.png'
img = Image.open(filename)
# img.show()
grayImg = img.convert('L')
# grayImg.show()
width, height = grayImg.size
image = np.array(grayImg)


cv2.line(image, (0, 0), (width, height), (255, 0, 0), 5)
cv2.line(image, (width, 0), (0, height), (255, 0, 0), 5)
cv2.namedWindow('myCats', cv2.WINDOW_NORMAL)
cv2.imshow('myCats', image)
cv2.imwrite('myCats.tiff', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

