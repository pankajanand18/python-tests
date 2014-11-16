__author__ = 'pankaj'


from fractions import  gcd
def getCommonDivisior(dataList):

    #dataList.sort()

    length = len(dataList)
    temp = 1
    g= dataList[0]
    while temp < length -1 and g!=1:
        #print g
        g = gcd(g,dataList[temp])
        temp +=1
    print g


tests=int(raw_input())

while  tests > 0:

    num_input=int(raw_input())
    dataListPlain = raw_input()
    dataListPlain = dataListPlain.split(' ')
    input_list=[]

    for data in dataListPlain:
        input_list.append(int(data))
        input_list.sort()
    if len(input_list) != num_input:
        raise AssertionError()


    getCommonDivisior(input_list)
    tests-=1

# input1=[5,15,10]
# input2=[3,1,2]
# input3=[15,9,6]
# getCommonDivisior(input1)
# getCommonDivisior(input3)
# getCommonDivisior(input2)



