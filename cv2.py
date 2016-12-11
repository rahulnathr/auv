import cv2 

cap=cv2.VideoCapture(0)

while(cap.isOpened()):
	ret,frame=cap.read()

	cv2.imshow('image',frame)

	k=cv2.waitKey(10) and 0xFF

	if k==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()