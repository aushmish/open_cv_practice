import cv2 as cv

img=cv.imread('Photos/cat2.jpeg')

def rescaleFrame(frame,Scale=0.75):
    width=int(frame.shape[1]*Scale)
    height=int(frame.shape[0]*Scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_img=rescaleFrame(img,0.2)
cv.imshow('NewImage',resized_img)

gray=cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

canny=cv.Canny(resized_img,125,175)
cv.imshow('Canny',canny)

Contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
cv.imshow('contours',Contours)

cv.waitKey(0)
cv.destroyAllWindows()