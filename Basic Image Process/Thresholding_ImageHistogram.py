import matplotlib.pyplot as plt
import numpy as np
import cv2


## import file


##file_path = filedialog.askopenfilename()


##image2 = cv2.imread(file_path) 

image2 = cv2.imread('lena1.jpg')

###

np_gray = np.zeros([np.size(image2,0), np.size(image2,1)])  ##def a gray picture's np


list_graycount=list()  #count of pixel number  -----colum
list_graynumber=list() #director of pixel      -----row

for i in range (0,256):     #update two np
    list_graycount.append(0)
    list_graynumber.append(i)

#   np visit
for i in range(0,np.size(image2,0)):
    for j in range(0,np.size(image2,1)):
        color_button=image2[i,j,0]*1+image2[i,j,1]*1+image2[i,j,2]*1
        color_button=color_button//3
        np_gray[i,j]=(color_button)
        list_graycount[color_button]=list_graycount[color_button]+1 #count pixel
                        
        color_button==0
        
np_gray=np_gray.astype(np.uint8)     ## int become uint8
        
cv2.imshow("Tracking", image2)    ##show img
cv2.waitKey(0)

cv2.imshow("Tracking", np_gray)   # show gray img
cv2.waitKey(0)

plt.ylabel("Accumulation")
plt.xlabel("Color scale")
plt.title("Histogram of image")

plt.bar(list_graynumber,list_graycount) #show 長條圖

plt.show()

