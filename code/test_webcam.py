import numpy as np
import cv2
import time
import sys 
args = sys.argv
    

cap = cv2.VideoCapture(0)
# cap.open()

if cap.isOpened():
	print("Cam opened")
else:
	print("could not open cam")

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FPS))

i = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    if (i % 30 == 0): #reduce framerate to 1FPS (for 30FPS input)
    	cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    i=i+1
# # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

