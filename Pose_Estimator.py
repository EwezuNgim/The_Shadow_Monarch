# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:28:00 2022

@author: root
"""
import cv2
import mediapipe as mp
import time
pTime=0
#pOse_Estimator --- Dtects 33 landmarks on the human body
mpPose=mp.solutions.pose
pose=mpPose.Pose()
Draw=mp.solutions.drawing_utils
'''params: self
          static_image_mode
          upper_body_only (T/F)
          smooth_landmark: True by default
          min_detection
          min_tracking

'''
cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    #Reading the feed from our webcam
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(image=imgRGB)
    #will help in the actual pose detection
    #print(results)
    #printing this would output a class, no actual data
    print(results.pose_landmarks)
    #However, this does
    if results.pose_landmarks:
        Draw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        #Image to be drawn on
        #coordinates to use
        #command to join coordinates together
        for id,ln in enumerate(results.pose_landmarks.landmark):
         h,w,c= img.shape
         print(id,ln)
         cx,cy=int(ln.x *w), int(ln.y * h)
         cv2.circle(img, (cx,cy), 5, (255,0,0),cv2.FILLED)
        
    cv2.imshow("Image",img)
    #dispaly feed
    cTime=time.time()
    fps=1/(cTime-pTime)
    #frame rate
    pTime=cTime
    
    #length of frame
    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    #third arg is the position of the origin
    
    cv2.waitKey(1)
