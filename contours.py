import cv2 as cv
import numpy as np




img = cv.imread('Photos/sign.png')

blank = np.zeros(img.shape[:2])

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125,127)

# thresholld to binarize the image
ret, thresh = cv.threshold(gray, 100,255,cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE )
print(len(contours))

# contours, hierarchy = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE )
# print(len(contours))

drawContours = cv.drawContours(blank, contours, -1, (255,0,0), thickness=1)


cv.imshow('contours', drawContours)

# cv.imshow('Cats',img)
# cv.imshow('blank', blank)
# cv.imshow('Gray', gray)
# cv.imshow('Blur',blur)
# cv.imshow('Canny',canny)
# cv.imshow('Thresh',thresh)



cv.waitKey(0)