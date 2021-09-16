import cv2 as cv
import numpy as np
import pytesseract 
import re
import json

img = cv.imread('0494188000.tif')

# cv.imshow("Image ",img)
	

def get_grayscale(img):
	return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def remove_noise(img):
	return cv.GaussianBlur(img, (3,3), 0)

def thresholding(img):
	return cv.threshold(img,0,255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

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


im_gray = get_grayscale(img)
im_thresh = thresholding(im_gray)



date_pattern = '^20\d\d$'
acc_no_pattern = '^\d{2}-\d{5}-\d-\d{2}$'
total_wages_pattern = '^\d{3}\s\d{2}$'


string_data = pytesseract.image_to_string(im_thresh)
# print(string_data)


# for viewing rect
# data_dict = pytesseract.image_to_data(im_thresh, output_type=pytesseract.Output.DICT)

# for box in range(n_boxes):
# 	if int(data_dict['conf'][box]) > 60:
# 		x,y,w,h = data_dict['left'][box],data_dict['top'][box],data_dict['width'][box],data_dict['height'][box]

# 		if re.match(acc_no_pattern, data_dict['text'][box]): 
# 			cv.rectangle(img, (x,y),((x+w),(y+h)), (0,255,0),2)
# 		elif re.match(date_pattern, data_dict['text'][box]): 
# 			cv.rectangle(img, (x,y),((x+w),(y+h)), (0,255,0),2)
	


# #for printing data 
data_dict = pytesseract.image_to_data(im_thresh, output_type=pytesseract.Output.DICT)
n_boxes = len(data_dict['text'])
# print(data_dict['text'])
data = {}
data_dict['text'].append("0xdeadbeef")

for box in range(n_boxes):

	if int(data_dict['conf'][box]) > 60:
		# print(data_dict['text'][box]+data_dict['text'][1+box])
		if re.match(acc_no_pattern, data_dict['text'][box]):
			data['account_number'] = data_dict['text'][box]
			print("Acc No:", data_dict['text'][box])

		elif re.match(date_pattern, data_dict['text'][box]):
			print("Date:", data_dict['text'][box])
			data['year'] = data_dict['text'][box]

		
		elif re.match(total_wages_pattern, data_dict['text'][box]+' '+data_dict['text'][1+box]):
			data['total_wages'] = data_dict['text'][box]+data_dict['text'][1+box]
			print("total wages:", data_dict['text'][box]+' '+data_dict['text'][1+box])



print(json.dumps(data))

# h,w,_ = img.shape
# boxes = pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
# 	b = b.split()
# 	img = cv.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
# print(boxes)



# cv.imshow("Box",img)
# cv.waitKey(0) & 0xFF==ord('d')

