import matplotlib.pyplot as plt
import numpy as np
import cv2




img = cv2.imread('test.jpg',0) 

###

np_gray = np.zeros([np.size(img,0), np.size(img,1)])  ##def a gray picture's np


list_graycount=list()  #count of pixel number  -----colum
list_graynumber=list() #director of pixel      -----row

for i in range (0,256):     #update two np
    list_graycount.append(0)
    list_graynumber.append(i)




#   np visit
for i in range(0,np.size(img,0)):
    for j in range(0,np.size(img,1)):

        color_button=img[i,j]
        np_gray[i,j]=(color_button)
        list_graycount[color_button]=list_graycount[color_button]+1 #count pixel
                        
        color_button==0
        
np_gray=np_gray.astype(np.uint8)     ## int become uint8



        
cv2.imshow("Tracking", img)    ##show img
cv2.waitKey(0)

for i in range(0,256):
   
       print("count:",list_graycount[i])
       print("pixel:",list_graynumber[i])
       print("\n")
