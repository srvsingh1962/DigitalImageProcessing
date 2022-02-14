import math
import numpy as np
import cv2
image = cv2.imread('srv.jpeg')
m,n,v = image.shape

gray_image = np.zeros((m,n),np.uint8)
image_onezeroes2 = np.zeros((m,n),np.uint8)

#***********TASK-1***************

Sum = 0
for i in range(m):
    for j in range(n):
        for k in range(v):
            Sum = Sum + image[i][j][k]
        gray_image[i][j] = math.floor(Sum/3)
        Sum = 0

#************Task-2***************

for v in range(m):
    for w in range(n):
        if(gray_image[v][w] >= 127):
            image_onezeroes2[v][w] = 1
        else:
            image_onezeroes2[v][w] = 0


cv2.imshow("original Image",image)
cv2.imwrite('Output/Image.jpeg',image)
cv2.waitKey(0)

cv2.imshow('Grayscale Image',gray_image)
cv2.imwrite('Output/gray_image.jpeg',gray_image)
cv2.waitKey(0)

cv2.imshow('Image with pixels 1 or 0',image_onezeroes2)
cv2.imwrite('Output/image_onezeroes2.jpeg',image_onezeroes2)
cv2.waitKey(0)

cv2.imshow('Grayscale image + Image with pixels 1/0',gray_image + image_onezeroes2)
cv2.imwrite('Output/gray_image + image_onezeroes2.jpeg',gray_image + image_onezeroes2)
cv2.waitKey(0)

cv2.imshow('Grayscale Image + 20 ',gray_image + 20)
cv2.imwrite('Output/gray_image+20.jpeg',gray_image + 20)
cv2.waitKey(0)

cv2.destroyAllWindows()