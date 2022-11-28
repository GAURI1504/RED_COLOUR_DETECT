# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:15:12 2021

@author: gauri
"""

import cv2
cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    r,g,b = cv2.split(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sub=cv2.subtract(gray, r)
    cv2.imshow('frame1',frame)
    cv2.imshow('frame2',gray)
    cv2.imshow('frame3',sub)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()