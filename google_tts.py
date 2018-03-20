import cv2
import numpy as np 
import sys

Maxdist = 5
# Sample image we took

cap = cv2.VideoCapture('hello1.mp4')
if(cap.isOpened()==False):
	print("err")

while(cap.isOpened()):
     ret,cap1 = cap.read()
     print(ret)
     print(cap1)
     if(ret==True):
       hsv = cv2.cvtColor(cap1,cv2.COLOR_BGR2HSV)

#Defining Ranges of blue color in hsv
       lower_blue = np.array([0,50,50])
       upper_blue = np.array([50,255,255])

#Thresholding only to obatin blue cvtColor
       mask=cv2.inRange(hsv, lower_blue, upper_blue)
       image,contours,hierarchy = cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
       contours1 = np.copy(contours)

  # Please this area is the main working code..
       max_area = 0
       largest_contour=-1
       for i in range(len(contours1)):
          contour = contours1[i]
          area = cv2.contourArea(contour)
          if(area>max_area) :
             max_area=area
             largest_contour=i
       h_contour = contours1[largest_contour]

# Please draw the lines in color RGB space
       cap_temp = cap1
       cv2.drawContours(cap1,contours,largest_contour,(0,255,0),20)
       cap0 = cv2.resize(cap1,(960,540))
       cv2.imshow('contour of cap',cap0)
       cv2.imwrite("Final.jpg",cap0)

       cap1 = cap_temp
       cap_temp = cv2.resize(cap_temp,(960,540))
       cv2.imshow('mask1',cap_temp)
       cv2.imwrite("Required.jpg",cap_temp)

       hull = cv2.convexHull(h_contour,returnPoints =False)
       hull_points =[]
       defects = cv2.convexityDefects(h_contour,hull)

       print(type(h_contour))
       print(h_contour)
       for i in range(defects.shape[0]) :
           s,e,f,d = defects[i,0]
           start = tuple(h_contour[s][0])
           hull_points.append(start)
           end = tuple(h_contour[e][0])
           far = tuple(h_contour[f][0])
           cv2.line(cap1,start,end,(0,255,0),5)
           cv2.circle(cap1,far,(0,0,255),10)
       cv2.imshow('finally.jpg',cap1)

       hull_points = 


     else:
        break
cap.release()
cv2.destroyAllWindows()
