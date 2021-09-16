import cv2 as cv
import pytesseract
from nltk import ngrams
import re
import pdb
# 0276704000 -- done
# 
image = cv.imread('Photos/0276704000.tif')
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image_strings = pytesseract.image_to_string(image)

account_pattern = r"\d{2}-\d{5}-\d-\d{2}"
year_pattern = r'(19|20)[0-9]{2}'
wages_pattern = r'[0-9][0-9,]*[0-9]\.?[0-9]{0,2}'

final_op = {
    "account": None,
    'year': None,
    'wages': None,
    
}

# for key, val in final_op.items():
#     if val == None:
sixgrams = ngrams(image_strings.split('\n'), 10)

# pdb.set_trace()

for key,value in final_op.items():
    for grams in sixgrams:
        line = ' '.join(grams)
        # print(line)
        if (key in line.lower()) & (value is None):
            # print(line)
            # print(key, line)
            if key == 'account':
                if re.search(account_pattern, line):
                    final_op[key] = re.search(account_pattern, line).group()
                    break
            elif key == 'year':
                if re.search(year_pattern, line.lower()):
                    final_op[key] = re.search(year_pattern, line).group()
                    break
            elif key == 'wages':
                if re.search(wages_pattern, line):
                    final_op[key] = re.search(wages_pattern, line).group()
                    break

print(final_op)