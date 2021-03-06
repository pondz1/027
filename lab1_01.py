import cv2
from PIL import Image

filename = 'Lemon.jpg'
image = cv2.imread(filename)
image2 = Image.open(filename)
height, width = image2.size
for x in range(0, width-1):
    image[x, x ] = (255, 0, 0)
cv2.line(image, (0, 0), (width, height), (255, 0, 0), 5)
cv2.namedWindow('Lemon', cv2.WINDOW_NORMAL)
cv2.imshow('Lemon', image)
cv2.imwrite('Lemon.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
