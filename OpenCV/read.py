import cv2 as cv
img=cv.imread('Photos/cat2.jpeg')
# cv.imshow('cat',img)
# cv.waitKey(0)

capture=cv.VideoCapture('videos/girl.mp4')

while True:
    isTrue,Frame=capture.read()
    cv.imshow('video',Frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()



