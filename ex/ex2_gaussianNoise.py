import numpy as np
import cv2
import random

img = cv2.imread('../airplane.tiff',1)

# Generate Gaussian noise
gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
# Add the Gaussian noise to the image
img_gauss = cv2.add(img,gauss)
# Display the image
cv2.imshow('a',img_gauss)
cv2.imwrite('../airplane_gauss.png',img_gauss)

#Speckle Noise
gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
noise = img + img * gauss
 
cv2.imshow('b',noise)
cv2.imwrite('../airplane_speckle.png',noise)

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

noise_img = sp_noise(img,0.05)
cv2.imshow('c',noise_img)
cv2.imwrite('../airplane_sp.png', noise_img)

cv2.waitKey(0)
