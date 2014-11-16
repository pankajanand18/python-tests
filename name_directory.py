__author__ = 'pankaj'
from operator import itemgetter

def formatName(input):

    def printName(personData):
        if personData[3] == 'M':
            return input("%s %s %s"%('Mr.',personData[0],personData[1]))
        else:
            return input("%s %s %s"%('Ms.',personData[0],personData[1]))
    return printName


@formatName
def showName(dataList):
    print dataList


n=int(raw_input())
temp = 0
input_list= []
while temp < n:
    temp+=1
    input_data= raw_input()
    input_data = input_data.split(" ")
    input_list.append(input_data)


input_list.sort(key=itemgetter(2))
for i in input_list:
    showName(i)

# showName(['Mike','Thomson',20,'M'])
# showName(['Lily','Thomson',20,'F'])

