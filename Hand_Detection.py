# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 10:18:19 2022

@author: User
"""
import cv2
import mediapipe
import time

cap=cv2.VideoCapture(0)
#we use an obj of 'VideoCapture' (cap) to get a video frame

mpHands=mediapipe.solutions.hands
hands= mpHands.Hands()
#params have to be inputted
#which: static_image_node can be False{is the default} (would detect or track based on confidence level) 
#or static  mode (detect only) which would make it slow
#min_detection_confidence equals to a num ber btw 0 and 1
#below that numbr it does the detection again 
#min_tracking_confidence

while True:
    success, ing=cap.read()
    #that'll capture/read the video frame
    ing = cv2.resize(ing, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #we want to send our RGB image to the object 'hands' but we have to 
    #convert it first bcoz hands uses only RGB images
    imgRGB=cv2.cvtColor(ing, cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    print(results.multi_hand_landmark)    
    
    cv2.imshow("Image",ing )
    #display the resulting frame
    cv2.waitKey(1)
    #determines how long a frame lasts. When arg is '1' it lasts for 1ms 
    #but '0', it lasts infinitely until you press a key
    
