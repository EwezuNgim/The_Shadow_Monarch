# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 15:22:51 2022

@author: User
"""
import mediapipe as mp
import cv2
import time#to check framerate
cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands(True)
npDraw=mp.solutions.drawing_utils
pTime=0
cTime=0
#Params:
'''static_image_mode(T/F: dets whether it traks or detects) whn False it switches btw both depnding on konfidens
   T:detects and is slowr
   max_num of hands
   min_detektion_confidence: below this val modl detekts
   min_traking_confidence:
    
    
    '''
while True:
    success, img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #We konvrt bkoz mp only uses RGB images
    results=hands.process(imgRGB)
    #processes frames, no display yet
    print(results.multi_hand_landmarks)
    #2 see if any hands are being dtkted
    
    #checking the no of hands
    if results.multi_hand_landmarks:
       for handlms in results.multi_hand_landmarks:
           #Want to extract ID and coordinates of hands 
           for id, ln in enumerate((handlms.landmark)):
            #print(id,ln)
            h,w,c=img.shape
            cx,cy=int(ln.x*w),int(ln.y*h)
            print(id,ln,(cx,cy))
            #ID, coordinates of hands, Pixl Position
            if id==0:
                cv2.circle(img,(cx,cy),25,(255,0,255),cv2.FILLED)
                #Draws a circl of thiknss 25 on ID=0 
            npDraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)
            #to draw the landMarks on feed from Webcam and connj
            
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    '''10,70 IS POSITION, 3 is skayl, 3 thiknss
    '''
    cv2.imshow('Image',img)
    cv2.waitKey(1)