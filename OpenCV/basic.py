import cv2 as cv
def rescaleFrame(frame,Scale=0.1):
    width=int(frame.shape[1]*Scale)
    height=int(frame.shape[0]*Scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


img=cv.imread('Photos/cat3.jpeg')
resizedImage=rescaleFrame(img)
cv.imshow('cat',resizedImage)

gray=cv.cvtColor(resizedImage,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur=cv.GaussianBlur(resizedImage,(7,7),cv.BORDER_DEFAULT)
cv.imshow('BLUR',blur)

# canny=cv.Canny(resizedImage,125,175)
# if you want to decrease the amount of few of the lines just use blur image insted of original one.....
canny=cv.Canny(blur,125,175)
cv.imshow('canny edges',canny)

dilated=cv.dilate(canny,(3,3),iterations=4)
cv.imshow('dilated image',dilated)  #it would just make it a bit thicker

eroded=cv.erode(dilated,(3,3),iterations=4)
cv.imshow('Eroded',eroded)#if you will pass the dilated one in the errode you will get canny one back

resized=cv.resize(img,(200,200),interpolation=cv.INTER_CUBIC) 
#CUBIC ka quality jyada accha hota hai , LINEAR bhi expand karega and  INTER_AREA will shrink 
cv.imshow('Resized',resized)

cropped=resizedImage[50:200,200:400]
cv.imshow('Cropped',cropped)
#this works on the principle of slicing as the numpy array is sliced

cv.waitKey(0)
