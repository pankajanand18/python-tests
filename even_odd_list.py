__author__ = 'pankaj'



def getEvenOddLists(ints):
    oddList=set()

    for i in ints:
        if i%2==0:
            continue
        else:
            oddList.add(i)
    print ints
    print oddList


ints = [1,21,53,84,50,66,7,38,9]
getEvenOddLists(ints)
