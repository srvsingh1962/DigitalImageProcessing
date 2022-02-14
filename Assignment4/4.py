import cv2

img_org = cv2.imread('srv.jpeg')
img_red = cv2.imread('srv.jpeg')
img_green = cv2.imread('srv.jpeg')
img_blue = cv2.imread('srv.jpeg')

img_blue[:,:,1],img_blue[:,:,2] = 0,0
img_green[:,:,0],img_green[:,:,2] = 0,0
img_red[:,:,0],img_red[:,:,1] = 0,0

cv2.imshow("Original Image",img_org)
cv2.imwrite('Output/Original Image.jpeg', img_org)
cv2.waitKey(0)

cv2.imshow("Reddish Image",img_red)
cv2.imwrite('Output/Reddish Image.jpeg', img_red)
cv2.waitKey(0)

cv2.imshow("Greenish Image",img_green)
cv2.imwrite('Output/Greenish Image.jpeg', img_green)
cv2.waitKey(0)

cv2.imshow("Blueish Image",img_blue)
cv2.imwrite('Output/Blueish Image.jpeg', img_blue)
cv2.waitKey(0)