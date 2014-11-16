__author__ = 'pankaj'



def isPallindrome(str,length):
    temp=0
    while temp <= length/2:
        if str[temp] != str[length-temp-1]:
            return False
        temp+=1

    return True

def checkPallindrome(str):

    if isPallindrome(str,len(str)) == True:
        return -1
    temp =0
    while temp < len(str):
        if str[temp] != str[-(temp+1)]:

            new_str=('%s%s')%(str[0:temp],str[temp+1:len(str)])
            if isPallindrome(new_str,len(new_str)) == True:
                return temp
            else:
                return len(str)-temp-1;
        temp+=1
        #print new_str

    return -1




n= int(raw_input())
temp = 0
while temp < n:
    temp+=1
    line = raw_input()
    print checkPallindrome(line)

# print isPallindrome("aa",2)
# print isPallindrome("aab",3)
#print isPallindrome("a",)





