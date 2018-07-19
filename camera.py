# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 19:12:26 2018

@author: romil
"""
import cv2
cap=cv2.VideoCapture(0)
while (1):
  ret, frame = cap.read()
  cv2.imshow('video1',frame)
    
  if cv2.waitKey(1) & 0xff == ord ('q') :
    break
      
cap.release()
cv2.destroyAllWindows()  