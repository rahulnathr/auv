import cv2 
import numpy as np 

def nothing(x):
	pass
cap=cv2.VideoCapture(1)

#create a black image,a window
#img=np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')
#Create trackbars for colour change 
cv2.createTrackbar('low_red','image',0,179,nothing)
cv2.createTrackbar('low_green','image',0,255,nothing)
cv2.createTrackbar('low_blue','image',0,255,nothing)
cv2.createTrackbar('up_red','image',0,179,nothing)
cv2.createTrackbar('up_green','image',0,255,nothing)
cv2.createTrackbar('up','image',0,255,nothing)
#create an on off switch
switch="0 :RED \n 1:GREEN \n 2:BLUE"
cv2.createTrackbar(switch,'image',0,2,nothing)

while (cap.isOpened()):
	ret,frame=cap.read()
	#convert from bgr to hsv
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	r=cv2.getTrackbarPos('low_red','image')
	g=cv2.getTrackbarPos('low_green','image')
	b=cv2.getTrackbarPos('low_blue','image')
	p=cv2.getTrackbarPos('up_red','image')
	q=cv2.getTrackbarPos('up_green','image')
	t=cv2.getTrackbarPos('up','image')
	

	s=cv2.getTrackbarPos(switch,'image')
	#for blue
	lower_blue=np.array([r,g,b])
	upper_blue=np.array([p,q,t])
	#find out the blue zone
	mask1=cv2.inRange(hsv,lower_blue,upper_blue)
	#superimpose the blue zone 
	res1=cv2.bitwise_and(frame,frame,mask=mask1)

	#for red
	lower_red=np.array([r,g,b])
	upper_red=np.array([p,q,t])

	#find the red zone 
	mask2=cv2.inRange(hsv,lower_red,upper_red)
	#superimpose the red 
	res2=cv2.bitwise_and(frame,frame,mask=mask2)

	#for green
	lower_green=np.array([r,g,b])
	upper_green=np.array([p,q,t])

	#find the green zone 
	mask3=cv2.inRange(hsv,lower_green,upper_green)
	#superimpose the green
	res3=cv2.bitwise_and(frame,frame,mask=mask3)




	if s==0:
		cv2.imshow('image',res2)
	k=cv2.waitKey(1) & 0xFF
	if k==27:
		break
	if s==1:
		cv2.imshow('image',res3)
	k=cv2.waitKey(1) & 0xFF
	if k==27:
		break

	if s==2:
		cv2.imshow('image',res1)
	k=cv2.waitKey(1) & 0xFF
	if k==27:
		break
		
cv2.destroyAllWindows()



