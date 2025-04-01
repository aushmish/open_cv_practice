import cv2 as cv
import numpy as np

img=cv.imread('Photos/boston.webp')
cv.imshow('Boston',img)

#translation:-
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x  left
# -y  up
#  y  down
#  x  right

translated=translate(img,100,100)
cv.imshow('translated image',translated)

#Rotations:-
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,45) # + rot => anti  , -ve rot => clockwise
cv.imshow('Rotated',rotated) 

again_rotate=rotate(rotated,-45)
cv.imshow('Rotation-2.0',again_rotate)

#flip:-

flipped=cv.flip(img,-1)
cv.imshow('Flip',flipped)

# 0 => flipping around the x-axis
# 1 => flipping around the y-axis(mirror image formation)
# -1 => both vertical and horizontal flip at the same time(mirror image but ulta me)

cv.waitKey(0)