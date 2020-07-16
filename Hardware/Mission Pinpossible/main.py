'''
Import CSV result from saleae logic analyzer software
'''

import csv
last = ''
display = ''
result = ''
word = None
last_word = None
with open('exported.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    data = [x[3] for x in reader]
    offset = 2
    for i in range(0,len(data),3):
        new = data[i] + data[i+1][2:] + data[i+2][2:]
        if last == '0x888C88' and new == '0x080C08':
            if display !=  '':
                print('\nResult on screen:')
                print(display)
                result += display[-1]
            display = ''
            word = None
            last_word = None
        else:
            if new[3] == '9' and new[5] == 'D' and new[7] == '9':
                word = new[:3]
            if word is not None and last_word is not None:
                display += bytes.fromhex(last_word[2:] + word[-1]).decode('utf-8')
                word = None
                last_word = None
        last = new
        last_word = word
print ('Code : ' + result)
