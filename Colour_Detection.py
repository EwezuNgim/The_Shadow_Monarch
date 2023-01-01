# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:21:46 2022

@author: User
"""
import cv2
import numpy as np
#img=cv2.imread('C:\\Users\\User\\Downloads\\809350.png')
#imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
def empty(a):
    pass
    

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',640,240)
cv2.createTrackbar('Hue Min','Trackbars',52,179,empty)
cv2.createTrackbar('Hue Max','Trackbars',79,179,empty)
cv2.createTrackbar('Sat Min','Trackbars',42,255,empty)
cv2.createTrackbar('Sat Max','Trackbars',146,255,empty)
cv2.createTrackbar('Val Min','Trackbars',24,255,empty)
cv2.createTrackbar('Val Max','Trackbars',168,255,empty)

while True:
    img=cv2.imread('C:\\Users\\User\\Downloads\\809350.png')
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos('Hue Min','Trackbars')
    s_min=cv2.getTrackbarPos('Sat Min','Trackbars')
    val_min=cv2.getTrackbarPos('Val Min','Trackbars')
    h_max=cv2.getTrackbarPos('Hue Max','Trackbars')
    s_max=cv2.getTrackbarPos('Sat Max','Trackbars')
    val_max=cv2.getTrackbarPos('Val Max','Trackbars')
    print(h_min,s_min,val_min)
    cv2.imshow('Original Image',img)
    cv2.imshow('Edit',imgHSV)
    cv2.waitKey(1)
    lower=np.array([h_min,s_min,val_min])
    upper=np.array([h_max,s_max,val_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgR=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('Mask',mask)
    cv2.imshow('AND',imgR)
    #WAS TRYING TO PUT ALL IMAGES IN THE SAME WINDOW
    #mask=mask * np.ones([3,3])
    #imgstak=np.hstack([img,imgHSV,imgR,mask])
    #cv2.inshow('ALL',imgstak)
    
#green:52,42,24,79,146,168
#blue:80,24,24,179,51,188

    
    
    
    

