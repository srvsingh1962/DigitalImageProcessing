import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('srv.jpeg',0)
_psnr = 10*np.log10((255*255)/(1/(225*225)*np.sum(img)*np.sum(img)))
print('PSNR is: ', _psnr)

def convert2binary(num):
    binary_num = [int(i) for i in list('{0:0b}'.format(num))]
    for j in range(8 - len(binary_num)):
        binary_num.insert(0,0)        
    return binary_num

def convert2decimal(listt):
    x = 0
    for i in range(8):
        x = x + int(listt[i])*(2**(7-i))
    return x

def discriminate_bit(bit,img):
    z = np.zeros([225,225])
    for i in range(225):
        for j in range(225):
            x = convert2binary(img[i][j])
            for k in range(8):
                if k == bit:
                    x[k] = x[k]
                else:
                    x[k] = 0
            x1 = convert2decimal(x)
            z[i][j] = x1
    return z

fig = plt.figure()
fig.set_figheight(15)
fig.set_figwidth(15)

for i in range(1,9):
    fig.add_subplot(4,2,i)
    plt.savefig('Output.jpeg')
    plt.imshow(discriminate_bit(i-1,img), cmap='gray')

plt.show(block=True)