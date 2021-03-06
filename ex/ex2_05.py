# Image Equalization
import cv2
import numpy as np
import matplotlib.pyplot as plt

def equalization(img):
    L=256
    x=list(range(0,L))
    p,bins=np.histogram(img,bins=256,range=(0,L))
    p=p/img.size
    plt.subplot('221')
    plt.plot(x,p)
    plt.title("Histogram")
    
    P=p.copy()
    out=np.zeros(img.shape,dtype=np.uint8)
    print(p.size,bins.size, P.size)
    for j in range(1,L):
        P[j] = P[j-1]+P[j]

    plt.subplot('223')
    plt.plot(x,P)
    plt.title("Cumulative Histogram")

    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            a=int(P[img.item(i,j)]*(L-1))
            out.itemset((i,j),a)

    s,bins=np.histogram(out,bins=256,range=(0,L))
    s=s/out.size
    plt.subplot('222')
    plt.plot(x,s)
    plt.title("Histogram")
    
    S=s.copy()
    print(s.size,bins.size, S.size)
    for j in range(1,L):
        S[j] = S[j-1]+S[j]

    plt.subplot('224')
    plt.plot(x,S)
    plt.title("Cumulative Histogram")
    plt.show()

    return out.astype(np.uint8)

filename='../house.tiff'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale',img)

img_eq=equalization(img)

cv2.namedWindow('Image Equalization', cv2.WINDOW_NORMAL)
cv2.imshow('Image Equalization',img_eq)

cv2.waitKey(0)
cv2.destroyAllWindows()
