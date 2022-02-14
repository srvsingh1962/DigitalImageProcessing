import math
import numpy as np
import cv2

a = np.zeros((512,512),np.uint8)
b = np.zeros((512,512),np.uint8)

a = cv2.circle(a,(235,250),80,(255,255,255),-1)            
b = cv2.rectangle(b,(100,300),(330,190),(255,255,255),-1)


#performing all logic gates operations and displaying the output images

cv2.imshow("white rectangle at center image",b)
cv2.imwrite('Output/white rectangle at center image.jpeg', b)
cv2.waitKey(0)

cv2.imshow("white circle at center image",a)
cv2.imwrite('Output/white circle at center image.jpeg', a)
cv2.waitKey(0)

cv2.imshow("AND operation",cv2.bitwise_and(a,b))
cv2.imwrite('Output/AND operation.jpeg', cv2.bitwise_and(a,b))
cv2.waitKey(0)

cv2.imshow("NAND operation",cv2.bitwise_not(cv2.bitwise_and(a,b)))
cv2.imwrite('Output/NAND operation.jpeg', cv2.bitwise_not(cv2.bitwise_and(a,b)))
cv2.waitKey(0)

cv2.imshow("OR operation",cv2.bitwise_or(a,b))
cv2.imwrite('Output/OR operation.jpeg', cv2.bitwise_or(a,b))
cv2.waitKey(0)

cv2.imshow("NOR operation",cv2.bitwise_not(cv2.bitwise_or(a,b)))
cv2.imwrite('Output/NOR operation.jpeg', cv2.bitwise_not(cv2.bitwise_or(a,b)))
cv2.waitKey(0)

cv2.imshow("XOR operation",cv2.bitwise_xor(a,b))
cv2.imwrite('Output/XOR operation.jpeg', cv2.bitwise_xor(a,b))
cv2.waitKey(0)

cv2.imshow("XNOR operation",cv2.bitwise_not(cv2.bitwise_xor(a,b)))
cv2.imwrite('Output/XNOR operation.jpeg', cv2.bitwise_not(cv2.bitwise_xor(a,b)))
cv2.waitKey(0)