import numpy as np
import cv2

image = cv2.imread('srv.jpeg')        
grayscaleimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

cv2.imshow("original Image",grayscaleimage)
cv2.imwrite('original Image.jpeg',grayscaleimage)
cv2.waitKey(0)

cv2.imshow("increase contrast Image",grayscaleimage*1.1)
cv2.imwrite('increase contrast Image.jpeg', grayscaleimage*1.1)
cv2.waitKey(0)

cv2.imshow("decrease contrast Image",grayscaleimage*0.0009)
cv2.imwrite('decrease contrast Image.jpeg', grayscaleimage*0.0009)
cv2.waitKey(0)

cv2.destroyAllWindows()