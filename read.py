import cv2 as cv
import pytesseract
import numpy as np

img = cv.imread('Photos/sign.png')

def gray(img):
	gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	return gray

def blur(img):
	blur = cv.GaussianBlur(img, (3,3), 0)
	return blur

def threshold(img):
	thresh = cv.threshold(img, 100, 125, cv.THRESH_BINARY)[1] 
	return thresh

# config for image_to_string
config = ('-l eng --oem 1 --psm 3')

im_gray = gray(img)
im_blur = blur(im_gray)
im_thresh = threshold(im_blur)

contours, heirarchy= cv.findContours(im_thresh, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

blank = np.zeros(img.shape[:2])

for i in range(len(contours)-10):
	drwcnt = cv.drawContours(blank,contours[i], -1, (77,124,38),thickness=1)
	cv.imshow("Contours",drwcnt)
	cv.waitKey(0)
# print(len(contours))
# cv.imshow("threshold",im_thresh)

