# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:36:07 2020

@author: USER
"""

import cv2
import numpy as np


image2 = cv2.imread('lena1.jpg')


np_mask = np.zeros([3,3])  #mask  usding to conclusion

np_gray = np.zeros([np.size(image2,0), np.size(image2,1)])  ##gray

np_threshold = np.zeros([np.size(image2,0), np.size(image2,1)])  ##threshold





#   np visit
for i in range(0,np.size(image2,0)):
    for j in range(0,np.size(image2,1)):
        color_button=image2[i,j,0]*1+image2[i,j,1]*1+image2[i,j,2]*1
        color_button=color_button//3
        np_gray[i,j]=(color_button)
        
        
        

        
np_gray=np_gray.astype(np.uint8)     ## int to uint8
np_threshold=np_threshold.astype(np.uint8)     ## int to uint8


        
cv2.imshow("Original", image2) 
cv2.waitKey(0)


cv2.imshow("gray", np_gray) 
cv2.waitKey(0)


for i in range(0,np.size(np_gray,0)):
    for j in range(0,np.size(np_gray,1)):
        
        
        if((i-1>=0)&(j-1>=0)&(i-1<=np.size(np_gray,0)-1)&(j-1<=np.size(np_gray,1)-1)): 
            np_mask[0,0]=np_gray[i-1,j-1]
        else:
            np_mask[0,0]=0
        
        if((i>=0)&(j-1>=0)&(i<=np.size(np_gray,0)-1)&(j-1<=np.size(np_gray,1)-1)): 
            np_mask[1,0]=np_gray[i,j-1]
        else:
            np_mask[1,0]=0
            
        if((i+1>=0)&(j-1>=0)&(i+1<=np.size(np_gray,0)-1)&(j-1<=np.size(np_gray,1)-1)): 
            np_mask[2,0]=np_gray[i+1,j-1]
        else:
            np_mask[2,0]=0
            
            
                      
            
        if((i-1>=0)&(j>=0)&(i-1<=np.size(np_gray,0)-1)&(j<=np.size(np_gray,1)-1)): 
            np_mask[0,1]=np_gray[i-1,j]
        else:
            np_mask[0,1]=0

        if((i>=0)&(j>=0)&(i<=np.size(np_gray,0)-1)&(j<=np.size(np_gray,1)-1)): 
            np_mask[1,1]=np_gray[i,j]
        else:
            np_mask[1,1]=0
            
        if((i+1>=0)&(j>=0)&(i+1<=np.size(np_gray,0)-1)&(j<=np.size(np_gray,1)-1)): 
            np_mask[2,1]=np_gray[i+1,j]
        else:
            np_mask[2,1]=0
            
            
            
            
        if((i-1>=0)&(j+1>=0)&(i-1<=np.size(np_gray,0)-1)&(j+1<=np.size(np_gray,1)-1)): 
            np_mask[0,2]=np_gray[i-1,j+1]
        else:
            np_mask[0,2]=0
            
        if((i>=0)&(j+1>=0)&(i<=np.size(np_gray,0)-1)&(j+1<=np.size(np_gray,1)-1)): 
            np_mask[1,2]=np_gray[i,j+1]
        else:
            np_mask[1,2]=0
            
        if((i+1>=0)&(j+1>=0)&(i+1<=np.size(np_gray,0)-1)&(j+1<=np.size(np_gray,1)-1)): 
            np_mask[2,2]=np_gray[i+1,j+1]
        else:
            np_mask[2,2]=0
            
            
            
            
            

        number=(np_mask[0,0]+np_mask[1,0]*2+np_mask[2,0]+np_mask[0,1]*2+np_mask[1,1]*4+np_mask[2,1]*2+np_mask[0,2]*1+np_mask[1,2]*2+np_mask[2,2])/16
        if(number<0):
            number=number*-1
        if(number>=255):
            number=255
        
        np_threshold[i,j]=number
        


        







cv2.imshow("convolution", np_threshold) 
cv2.waitKey(0)



