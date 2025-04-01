import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#paint the image a certain color:-(b,g,r)
# blank[:]=255,100,0

# blank[100:150,100:200]=0,0,255 # [rowindex,column index](100 x 100 pixel)
# cv.imshow('Green',blank)

# rectangle:-
# cv.rectangle(blank,(0,0),(500,250),(0,255,0),thickness=4)
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=cv.FILLED)
# cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)

#square:-
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
cv.imshow('square',blank)

#circleP:-
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1) #-1 will fill the image
cv.imshow('circle',blank)


#line:-
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)
# cv.line(blank,(100,250),(300,400),(255,0,0),thickness=3)
cv.imshow('line',blank)

#writing Text:-
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)
cv.waitKey(0)