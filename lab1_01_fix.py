import cv2
from PIL import Image

filename = 'Lemon.jpg'
image = cv2.imread(filename)
image2 = Image.open(filename)
width,height = image2.size
rx,ry = 1,1
if height>width:
    ry = height/width
    for x in range(0, width - 1):
        image[int(x * ry), int(x * rx)] = (255, 0, 0)
else:
    rx = width/height
    for x in range(0, height-1):
        image[int(x*rx), int(x*ry) ] = (255, 0, 0)
# cv2.line(image, (0, 0), (width, height), (255, 0, 0), 5)
cv2.namedWindow('Lemon', cv2.WINDOW_NORMAL)
cv2.imshow('Lemon', image)
cv2.imwrite('Lemon.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
