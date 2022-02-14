import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('srv.jpeg')
m,n,v = np.shape(image)

grayscaleimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayscaleimage_1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
unique_array = np.unique(grayscaleimage)
count_array = np.zeros(len(unique_array),int)
cdf_array = np.zeros(len(unique_array),int)
hv_array = np.zeros(len(unique_array),int)

for i in range(0,len(unique_array)):
    count_array[i] = np.count_nonzero(grayscaleimage == unique_array[i])

cdf_array[0] = count_array[0]

for i in range(1,len(unique_array)):
    cdf_array[i] = cdf_array[i-1] + count_array[i]

cdf_min = min(cdf_array)

for i in range(0,len(unique_array)):
    hv_array[i] = round(((cdf_array[i] - cdf_min)*255)/((m*n) - cdf_min))

for i in range(0,len(unique_array)):
    for j in range(m):
        for k in range(n):
            if(grayscaleimage_1[j][k] == unique_array[i]):
                grayscaleimage_1[j][k] = hv_array[i]
            else:
                continue


print("m x n x v  = %d x %d x %d"%(m,n,v))
print("grayscaleimage =")
print(grayscaleimage)
print("unique_array =")
print(unique_array)
print("count_array =")
print(count_array)
print("cdf_array =")
print(cdf_array)
print("cdf_min = %d"%(cdf_min))
print("hv_array =")
print(hv_array)
print("grayscaleimage_1 =")
print(grayscaleimage_1)

cv2.imshow('Image before histogram equalization',grayscaleimage)
cv2.imwrite('Output/Image before histogram equalization.jpeg', grayscaleimage)
cv2.waitKey(0)

cv2.imshow('Image after histogram equalization with algorithm discussed in class',grayscaleimage_1)
cv2.imwrite('Image after histogram equalization with algorithm discussed in class.jpeg', grayscaleimage_1)
cv2.waitKey(0)

cv2.imshow('Image after histogram equalization with direct function',cv2.equalizeHist(grayscaleimage))
cv2.imwrite('Image after histogram equalization with direct function.jpeg', cv2.equalizeHist(grayscaleimage))
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(3,1,1)
plt.hist(grayscaleimage.ravel(),256,[0,256])
plt.subplot(3,1,2)
plt.hist(grayscaleimage_1.ravel(),256,[0,256])
plt.subplot(3,1,3)
plt.hist(cv2.equalizeHist(grayscaleimage).ravel(),256,[0,256])
plt.savefig('outputPlot.jpeg')
plt.show()