import cv2 as cv

#this rescale method will work with photos , videos as well as live videos 
def rescaleFrame(frame,Scale=0.75):
    width=int(frame.shape[1]*Scale)
    height=int(frame.shape[0]*Scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


#reading images:-
image=cv.imread('Photos/cat2.jpeg')
cv.imshow('cat',image)
resized_image=rescaleFrame(image,0.2)
cv.imshow('Cat',resized_image)

#this method is gonna work well with live videos (for the videos from the external sources):-
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

#reading videos:-

capture=cv.VideoCapture('videos/girl.mp4')
while True:
    isTrue,Frame=capture.read()
    frameResized=rescaleFrame(Frame,0.2)
    # cv.imshow('video',Frame)
    cv.imshow('vidio1',Frame)
    cv.imshow('video',frameResized)

    if cv.waitKey(5) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
