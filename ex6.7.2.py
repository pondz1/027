import cv2
from matplotlib import interactive, pyplot as plt

B1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
B2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
B3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

print('B1 (MORPH_RECT) = \n', B1)
print('B2 (MORPH_CROSS) = \n', B2)
print('B3 (MORPH_ELLIPSE) = \n', B3)


img = cv2.imread(
    './DIP3E_Original_Images_CH09/Fig0905(a)(wirebond-mask).tif', 0)
dst_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, B1, iterations=1)
dst_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, B2, iterations=1)

# เพิ่มการดำเนินการทำ Dilation, Erosion, Open & Close โดยใช้ SE เหมือน B2,ฺB3 ให้ครบทุกตัว

dst_dilation_B2 = cv2.morphologyEx(img, cv2.MORPH_DILATE, B2, iterations=1)
dst_dilation_B3 = cv2.morphologyEx(img, cv2.MORPH_DILATE, B3, iterations=1)

dst_eros_B2 = cv2.morphologyEx(img, cv2.MORPH_ERODE, B2, iterations=1)
dst_eros_B3 = cv2.morphologyEx(img, cv2.MORPH_ERODE, B3, iterations=1)

dst_open_B2 = cv2.morphologyEx(img, cv2.MORPH_OPEN, B2, iterations=1)
dst_open_B3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, B3, iterations=1)

dst_close_B2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, B2, iterations=1)
dst_close_B3 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, B3, iterations=1)

titles = ['Original Ex', 'Opening Ex', 'Closing Ex',
          'Dilation B2', 'Dilation B3', 'Erosion B2',
          'Erosion B3', 'Opening B2', 'Opening B3',
          'Close B2', 'close B3']
images = [img, dst_open, dst_close,
          dst_dilation_B2, dst_dilation_B3, dst_eros_B2,
          dst_eros_B3, dst_open_B2, dst_open_B3,
          dst_close_B2, dst_close_B3]
for i in range(len(images)):
    plt.subplot(4, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
