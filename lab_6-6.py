# Boundary Extraction 𝛽(𝐴) = 𝐴 − (𝐴⊝𝐵) และ Gradient boundary
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(
    './DIP3E_Original_Images_CH09/Fig0914(a)(licoln from penny).tif', 0)

kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dst_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal, iterations=1)

dst_eros = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernal, iterations=1)

dst_extraction = cv2.subtract(img,dst_eros)

titles = ['Origin', 'Boundary Extraction', 'Gradient']
images = [img, dst_extraction, dst_gradient]
for i in range(len(images)):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
