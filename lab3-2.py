import cv2
import numpy as np

matrix = [[10, 4, 22], [2, 18, 7], [9, 4, 25]]
result = np.zeros((6, 6))
for i in range(3):
    for j in range(3):
        for k in range(2):
            for l in range(2):
                result[k+i, l+i] = matrix[i][j]

print(result)
