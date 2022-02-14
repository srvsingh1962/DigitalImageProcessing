import numpy as np
import cv2

image = cv2.imread("srv.jpeg")

m,n,v = image.shape  
Increased_contrast = np.zeros(image.shape, image.dtype)
Decreased_contrast = np.zeros(image.shape, image.dtype)

alpha_1 = 1.6
alpha_2 = 0.7
beta = 0

for y in range(image.shape[0]):
    for x in range(image.shape[1]): 
        for c in range(image.shape[2]):
            Decreased_contrast[y,x,c] = np.clip((alpha_2*image[y,x,c]) + beta, 0, 255) 
            Increased_contrast[y,x,c] = np.clip((alpha_1*image[y,x,c]) + beta, 0, 255)

cv2.imshow("Original",image)
cv2.imwrite("Original.jpeg",image)
cv2.imshow("Contrast Increased", Increased_contrast)
cv2.imwrite("Contrast Increased.jpeg",Increased_contrast)
cv2.imshow("Contrast Decreased", Decreased_contrast)
cv2.imwrite("Contrast Decreased.jpeg",Decreased_contrast)
cv2.waitKey(0)

cv2.destroyAllWindows()