__author__ = 'pankaj'

input_array='abcdefghijklmnopqrstuvwxyz'

def check_panagrams(str):
    global input_array
    str=str.lower()
    for ch in input_array:
        if str.find(ch)==-1:
            return False

    return  True


input_line= raw_input()

if check_panagrams(input_line) == True:
    print 'pangram'
else:
    print 'not pangram'


