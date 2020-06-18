import numpy as np
import cv2

img1=cv2.imread('C:/Users/Anshuman/Pictures/2019-06/1523841341135.jpg')
cv2.imshow('img1',img1)
cv2.waitKey(10)

img2=cv2.imread('C:/Users/Anshuman/Pictures/2019-06/1523841341135.jpg')
cv2.imshow('img2',img2)
cv2.waitKey(10)

x=np.uint8([250])
y=np.uint8([10])
print(cv2.add(x,y))

img1=cv2.imread('C:/Users/Anshuman/Pictures/2019-06/1523841341135.jpg')
img2=cv2.imread('C:/Users/Anshuman/Pictures/2019-06/1523841341135.jpg')
dst=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('IMAGE_BLENDING',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
