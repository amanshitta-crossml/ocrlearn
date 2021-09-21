import cv2 as cv
import pytesseract
import re 
from nltk import ngrams
from fuzzywuzzy import fuzz

img = cv.imread('Photos/0276704000.tif')

image_data = ' '.join(pytesseract.image_to_string(img).split())


# # writing image data to file
# with open('image_data', 'w') as f:
#     f.write(' '.join(image_data.split()))

def find_data_and_dict(to_find, ptr, gram_len):
    n_gram = list(ngrams(image_data.split(), gram_len))
    
    for i, gram in enumerate(n_gram):
        #print(gram)
        # print(i, ' '.join([w.lower() for w in gram]), gram_len)
        if fuzz.partial_ratio(to_find, ' '.join([w.lower() for w in gram])) > 90:
            print("gram",gram)
            print("gram len",len(gram))
            
            print(image_data.split()[i:i+len(gram)*len(gram)])
            # print(fuzz.partial_ratio(to_find, ' '.join([w.lower() for w in gram])))
            if i < len(n_gram)-3:
                line = ' '.join(image_data.split()[i:i+len(gram)*len(gram)])
                # print("N gram : ",n_gram[i:i+2], to_find)
                pass
            # else:
            #     line = ' '.join(tup for tup in  (n_gram[i:-1]))
            # print(line)
            if re.search(ptr, line):
                return re.search(ptr, line).group()
    return None



account_pattern = r"\d{2}-\d{5}-\d-\d{2}"
year_pattern = r'\s(19|20)[0-9]{2}\s'
wages_pattern = r'[0-9][0-9,]*[0-9](\.|\s)?[0-9]{2}'

final_op = {
    "account": None,
    'year': None,
    'wages': None,
    # 'due_date': None
}
keys = list(final_op.keys())

to_find_list = ['mo employer account no', 'year','total wages paid']

for i,to_find in enumerate(to_find_list):
    gram_len = len(to_find.split())
    if 'account' in to_find:
        # print(to_find)
        ptr = account_pattern  
    elif 'year' in to_find:
        # print(to_find)
        ptr = year_pattern
        
    elif 'wages' in to_find:
        ptr = wages_pattern
        # print(to_find)
    # print("called")
    final_op[keys[i]] = find_data_and_dict(to_find, ptr, gram_len)

print(final_op)