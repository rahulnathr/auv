import cv2 
import numpy as np 
def nothing(X):
	pass

cap=cv2.VideoCapture(1)

cv2.namedWindow('image')
cv2.createTrackbar('Min','image',0,100,nothing)
cv2.createTrackbar('Max','image',0,110,nothing)
while (cap.isOpened()):
	ret,frame=cap.read()

	#image=cv2.imread('reef.jpg',1)
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#display the resulting frame 
#normalise the frame 
#cv2.namedWindow('origin',cv2.WINDOW_NORMAL)
#cv2.namedWindow('gray',cv2.WINDOW_NORMAL)
#cv2.namedWindow('equal',cv2.WINDOW_NORMAL)

	x=cv2.getTrackbarPos('Min','image')
	y=cv2.getTrackbarPos('Max','image')
	canny=cv2.Canny(gray,x,y)
	cv2.imshow('image',canny)
	
	k=cv2.waitKey(1) & 0xFF
	if k==27:
		break
cv2.destroyAllWindows()
