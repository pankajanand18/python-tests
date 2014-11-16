__author__ = 'pankaj'


def getPallindromeCount(string):

    mid=0
    right=0
    left=0
    counter =0
    longest_length=0
    while mid < len(string):
        right=mid
        left=mid
        found =  True
        while right >=0 and left < len(string):
            if string[right] == string[left]:
                if left - right >longest_length:
                    longest_length= left-right
                    counter=1
                elif left-right == longest_length:
                    counter+=1
            else:
                break

            left+=1
            right-=1



        right=mid
        left=mid+1
        while right >=0 and left < len(string):
            if string[right] == string[left]:
                if left - right >longest_length:
                    longest_length= left-right
                    counter=1
                elif left-right == longest_length:
                    counter+=1
            else:
                break

            left+=1
            right-=1






        mid+=1
    print longest_length
    print counter


getPallindromeCount('ababbacababbad')
# tests=int(raw_input())
#
# while  tests > 0:
#     t=raw_input()
#
#     tests-=1


