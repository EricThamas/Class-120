from typing import Final
import cv2 
import numpy as np
cap=cv2.VideoCapture(0)
back=cv2.imread("Background.png")
while cap.isOpened():
    dummy,frame=cap.read()
    #print(dummy)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # red=np.unit8([[[0,0,255]]])
    lowerRed1=np.array([0,120,60])
    upperRed1=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lowerRed1,upperRed1)

    lowerRed2=np.array([170,120,70])
    upperRed2=np.array([170,180,255])
    mask2=cv2.inRange(hsv,lowerRed2,upperRed2)
    mask_1=mask1+mask2
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask_1=cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    #creating mask2 the color range outside the red color
    mark2=cv2.bitwise_not(mask_1)
    part1=cv2.bitwise_and(frame,frame,mask=mask2)
    part2=cv2.bitwise_and(back,back,mask=mask_1)
    FinalOutput=cv2.addWeighted(part1,1,part2,1,0)
    if dummy:
        cv2.imshow("camera",FinalOutput)
        if cv2.waitKey(5)==ord("q"):
            break
cap.release()
cv2.destroyAllWindows()    