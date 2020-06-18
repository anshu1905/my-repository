import cv2
import numpy as np

def nothing(x):
    pass
cap=cv2.VideoCapture(0)

#create a black image into a window
img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('hue','image',0,180,nothing)
cv2.createTrackbar('sat','image',0,255,nothing)
cv2.createTrackbar('val','image',0,255,nothing)


while(True):
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    k=cv2.waitKey(100)
    if k==27:
        break

    #get current position of four trackbars
    h=cv2.getTrackbarPos('hue','image')
    s=cv2.getTrackbarPos('sat','image')
    v=cv2.getTrackbarPos('val','image')
    
    lower=np.array([h,s,v])
    upper_range=np.array([180,255,255])
    mask=cv2.inRange(hsv,lower,upper_range)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    
cv2.destroyallwindows()


