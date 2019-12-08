import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('video capture', gray)
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

