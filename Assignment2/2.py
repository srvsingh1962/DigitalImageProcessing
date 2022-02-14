import math
import numpy as np
import cv2

image = cv2.imread('srv.jpeg')
m,n,v = image.shape

gray_image = np.zeros((m,n),np.uint8)
gray_image2 = np.zeros((m,n),np.uint8)  
image_onezeroes2 = np.zeros((m,n),np.uint8)

#Converting Color image to gray scale
Sum = 0
for i in range(m):
    for j in range(n):                            
        for k in range(v):
            Sum = Sum + image[i][j][k]
        gray_image[i][j] = math.floor(Sum/3)
        Sum = 0

for x in range(m):
    for y in range(n):
        gray_image2[x][y] = gray_image[x][y]

#making some part of gray scale image to black
for x in range(20,300,1):
   for y in range(50,300,1):
       gray_image2[x][y] = 0

cv2.imshow("original Image",image)
cv2.imwrite('Output/image.jpeg', image)
cv2.waitKey(0)

cv2.imshow('Grayscale Image',gray_image)
cv2.imwrite('Output/gray_image.jpeg', gray_image)
cv2.waitKey(0)

cv2.imshow('Grayscale Image2',gray_image2)
cv2.imwrite('Output/gray_image2.jpeg', gray_image2)
cv2.waitKey(0)

cv2.imshow('Grayscale Image - Grayscale Image2',abs(gray_image - gray_image2))
cv2.imwrite('Output/Grayscale Image - Grayscale Image2.jpeg',abs(gray_image - gray_image2))
cv2.waitKey(0)