import cv2
import numpy as np

A = np.array([
    [0, 0, 0, 0], [0, 1, 0, 0],
    [0, 1, 1, 0], [0, 0, 1, 0],
    [0, 0, 0, 0]], np.uint8)
B = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], np.uint8)

print('A = ', A, end='\n')
print('B = ', B, end='\n')

C = cv2.dilate(A, B, iterations=1,
               borderType=cv2.BORDER_CONSTANT, borderValue=0)

print('Dilate (C=A dilated by B) = \n', C, end='\n')

C = cv2.erode(C, B, iterations=1,
              borderType=cv2.BORDER_CONSTANT, borderValue=0)
print('Erosion (C eroded by B) = \n', C, end='\n')

######## Square ###################################################

B = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 0]], np.uint8)

C = cv2.dilate(A, B, iterations=1,
               borderType=cv2.BORDER_CONSTANT, borderValue=0)

print('Dilate (C=A dilated by B) = \n', C, end='\n')

C = cv2.erode(C, B, iterations=1,
              borderType=cv2.BORDER_CONSTANT, borderValue=0)
print('Erosion (C eroded by B) = \n', C, end='\n')

######## Cross ###################################################

B = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)

C = cv2.dilate(A, B, iterations=1,
               borderType=cv2.BORDER_CONSTANT, borderValue=0)

print('Dilate (C=A dilated by B) = \n', C, end='\n')

C = cv2.erode(C, B, iterations=1,
              borderType=cv2.BORDER_CONSTANT, borderValue=0)
print('Erosion (C eroded by B) = \n', C, end='\n')
