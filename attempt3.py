import cv2 as cv
import pytesseract
from nltk import ngrams
import re
import pdb

file_list = ['0276704000.tif','0279062000.tif', '0281217000.tif','0282274000.tif','0494188000.tif','0230551000.tif', '0235100000.tif', \
    '0240281000.tif','0245808000.tif', '0253651000.tif', '0256958000.tif', '0261918000.tif', \
        '0264014000.tif', '0269779000.tif', '0273072000.tif']
print(file_list)

i = input("Enter from index")
print(file_list[int(i)-1])
image = cv.imread(f'Photos/{file_list[int(i)-1]}')

image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image_strings = pytesseract.image_to_string(image)

image_strings = image_strings.replace('\n',' ')

account_pattern = r"\d{2}-\d{5}-\d-\d{2}"
year_pattern = r'\s(19|20)[0-9]{2}\s'
wages_pattern = r'[0-9][0-9,]*[0-9](\.|\s)?[0-9]{2}'

final_op = {
    "account": None,
    'year': None,
    'wages': None,
    
}

def find_data_and_dict(key, pattern):
    sixgrams = ngrams(image_strings.split(), 10)
    for grams in sixgrams:
            line = ' '.join(grams)
            
            if (key in line.lower()) & (value is None):
                print(key,line)
                if re.search(pattern, line):
                    final_op[key] = re.search(pattern, line).group().strip()
                    break

for key,value in final_op.items():
    if key == 'account':
        
        find_data_and_dict(key, account_pattern)
    elif key == 'year':
        
        find_data_and_dict(key, year_pattern)
       
    elif key == 'wages':
        
        find_data_and_dict(key, wages_pattern)
        
                              
print(final_op)