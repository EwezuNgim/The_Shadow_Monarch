# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 03:27:26 2022

@author: root
"""
import cv2
import mediapipe as mp
import time
mpFace=mp.solutions.face_mesh
Draw=mp.solutions.drawing_utils
face=mpFace.FaceMesh()
#this  is an ob jec t  of  the  face mesh  class
#only  an  object can use  'process'
#if you use  a  var it'll  ask you  for  self
cap=cv2.VideoCapture(0)
pTime=0

while True:
    successful,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #print(type(imgRGB))
    result=face.process(image=imgRGB)
    if result.multi_face_landmarks:
       print(result.multi_face_landmarks)
       for i  in result.multi_face_landmarks :
            
        for id,ln in enumerate(i.landmark):
            h,w,c=img.shape
            cx,cy=int(ln.x *w),int(ln.y*h)
            cv2.circle(img,(cx,cy),10,(255,0,255),cv2.FILLED)
            #image, centre point, thickness of line, colour of line
            #Draw.draw_landmarks(img,result.multi_face_landmarks.landmark,mpFace.FACEMESH_TESSELATION)
            Draw.draw_landmarks(img,i,mpFace.FACEMESH_TESSELATION)
            
            
            
    
    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0))
    cv2.imshow('Image',img)
    
    cv2.waitKey(1)
    
