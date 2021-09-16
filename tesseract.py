import cv2 as cv
import pytesseract
import numpy as np

img = cv.imread('Photos/invoice.jpg')


def view(name,img):
	cv.imshow(name, img)
	cv.waitKey(0)

def get_grayscale(img):
	return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def remove_noise(img):
	return cv.GaussianBlur(img, (3,3), 0)

def thresholding(img):
	return cv.threshold(img,0,255, cv.THRESH_BINARY + cv.THRESH+_OTSU)[1]

def dilate(img):
	kernel = np.ones((5,5), dtype='uint8')
	return cv.dilate(img, kernel, iterations=1)

def erode(img):
	kernel = np.ones((5,5), dtype='uint8')
	return cv.erode(img, (kernel), iterations=1)

def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def canny(image):
    return cv2.Canny(image, 100, 200)

def match_template(img, template):
	return cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)


# # rect around word

d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
boxes = len(d['text'])

for i in range(boxes):
    if int(d['conf'][i]) > 40:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1
)
view("boxes", img)



# # rectangle around text 
# h,w,c = img.shape

# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
# 	# d 188 951 198 961 0
# 	b = b.split(' ')
# 	img = cv.rectangle(img, (int(b[1]),h-int(b[2])), (int(b[3]), h-int(b[4])), (0,255,0),2)
# view("rect",img)

