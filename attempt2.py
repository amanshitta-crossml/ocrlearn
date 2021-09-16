import cv2 as cv
import pytesseract
import re
import numpy as np
from fuzzywuzzy import fuzz
import pdb 



img = cv.imread('Photos/0494188000.tif')
# print(img.shape)
# img = cv.resize(img, None, fx=0.5, fy=0.45)
smooth = cv.GaussianBlur(img, (3, 3), 0)
gray = cv.cvtColor(smooth, cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape[:2], dtype='uint8')

account_pattern = r"\d{2}-\d{5}-\d-\d{2}"
year_pattern = r'(19|20)[0-9]{2}'
wages_pattern = r'[0-9,\.\$\s]{1,25}'

final_op = {
    'year': None,
    'wages': None,
    "account": None,
}

data_dict = pytesseract.image_to_data(
    img, output_type=pytesseract.Output.DICT)
n_boxes = len(data_dict['text'])
print(data_dict)
string_data = pytesseract.image_to_string(img)

# account - new_x, new_y, new_w, new_h = x-250,y-20,x+120,y+60
# year = new_x, new_y, new_w, new_h = x-200,y-20,x+150,y+100
for key,val in final_op.items():
    # print(key, val)
    if not val:
        for i in range(n_boxes):
            
            if fuzz.ratio(data_dict['text'][i].lower(), key) > 70:
                print((data_dict['text'][i], f" {key} ",str(fuzz.ratio(data_dict['text'][i].lower(), key))))
                x,y,w,h = data_dict['left'][i], data_dict['top'][i], \
                    data_dict['width'][i], data_dict['height'][i]
                
                new_x, new_y, new_w, new_h = x-200,y-80,x+120,y+100
                # print(new_x,new_y,new_w,new_h)
                rect = img[new_y:new_h,new_x:new_w]
                cv.imshow(key,rect)
                cv.waitKey(0)
                account_box_data = pytesseract.image_to_string(rect)
                # print(account_box_data)
                # pdb.set_trace()

                matched = re.search(account_pattern, account_box_data)
                if matched:
                    final_op[key] = matched.group()
                    break
                
                # print(" after "+ str(i))
print(final_op)
                # print(re.findall(account_pattern,account_box_data))



    

# for box in range(n_boxes):
#     # print(data_dict['text'][box], data_dict['conf'][box])
#     if int(data_dict['conf'][box]) > 75:
#         if fuzz.ratio(data_dict['text'][box].lower(),'total wages') > 75:
#             print(data_dict['text'][box])
#             # x, y, w, h = data_dict['left'][box], data_dict['top'][box]\
#             #     , data_dict['left'][box], data_dict['top'][box]
        