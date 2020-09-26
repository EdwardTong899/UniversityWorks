import cv2
import numpy as np


image2 = cv2.imread('30.jpg')




np_gray = np.zeros([np.size(image2,0), np.size(image2,1)])  ##gray

np_threshold = np.zeros([np.size(image2,0), np.size(image2,1)])  ##threshold

np_projector=np.zeros([np.size(image2,0)+50, np.size(image2,1)+50])

np_count_vertical=np.zeros([np.size(image2,0)]) ##垂直投影累計值

np_count_horizontal=np.zeros([np.size(image2,1)]) ##水平投影累計值

#############   binary process ######################
for i in range(0,np.size(image2,0)):
    for j in range(0,np.size(image2,1)):
        color_button=image2[i,j,0]*1+image2[i,j,1]*1+image2[i,j,2]*1
        color_button=color_button//3
        np_gray[i,j]=(color_button)
        
        
        
        
        if (color_button>=150):                        ##threshold=150
            np_threshold[i,j]=255
        else:
            np_threshold[i,j]=0
            
                      
        color_button==0
#######################################################        
np_gray=np_gray.astype(np.uint8)     ## int to uint8
np_threshold=np_threshold.astype(np.uint8)     ## int to uint8




################ show image ##########################        
cv2.imshow("Tracking", image2) 
cv2.waitKey(0)



cv2.imshow("Tracking", np_threshold) 
cv2.waitKey(0)

######################################################



###############  count total pixel about projection ###############
for i in range(0,np.size(image2,0)):
    for j in range(0,np.size(image2,1)):
        np_projector[i][j]=np_threshold[i][j]
        if(np_projector[i][j]==0):
            np_count_vertical[i]=np_count_vertical[i]+1
            np_count_horizontal[j]=np_count_horizontal[j]+1
            
#####################################################################
            
np_projector=np_projector.astype(np.uint8) 

cv2.imshow("Tracking", np_projector) 
cv2.waitKey(0)           




################### draw projection ################################
for i in range(0,np.size(image2,1)):
    a=int(np_count_horizontal[i]/np.size(np_projector,0)*50)
    
    for j in range(np.size(np_projector,0)-1-a,np.size(np_projector,0)-1):
       np_projector[j][i]=255
     

cv2.imshow("Tracking", np_projector) 
cv2.waitKey(0)


for i in range(0,np.size(image2,0)):
    a=int(np_count_vertical[i]/np.size(np_projector,1)*50)
    
    for j in range(np.size(np_projector,1)-1-a,np.size(np_projector,1)-1):
       np_projector[i][j]=255
       
######################################################################       
cv2.imshow("Tracking", np_projector) 
cv2.waitKey(0)    
       
