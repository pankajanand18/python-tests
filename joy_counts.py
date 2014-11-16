import yappi
import math

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def mergelist(a,b):
    count = len(b) -1
    while count >= 0:
        a.pop()
        count-=1
    a.extend(b)
    return a


# a=[1,2,3,]
# b=[5,6,3,4]
# print mergelist(a,b)

# def getkthelementrecursiveDriver(k):
#     list = getkthelementrecursive(k)
#     for i in list:
#         print i,
#     print ''


initial_list=[2,3,4]



def getkthElementIterative(k,array=None):
    global initial_list
    if k < 4:
        return [initial_list[k-1]]

    power_list=[1]
    boundry_list=[(0,3)]

    num = bucket_start= j= num_trail = 3
    element_count=1
    while j < k:
        num_trail = num
        power_list.append(num_trail)
        bucket_start = j
        num = num * 3
        j += (num)
        bucket_end = j
        boundry_list.append((bucket_start,bucket_end))
        element_count+=1

    data_list = [2] * element_count
    temp = 0
    offset = k - bucket_start
    while  temp < element_count and offset > 0:

        num_trail= power_list[element_count-1-temp]
        data_list[temp]= initial_list[ ((offset-1)/num_trail) ]
        temp +=1
        new_offset=  (bucket_start - num_trail) + ( offset - ((num_trail)*((offset-1)/num_trail)))
        bucket_start = boundry_list[element_count-1-temp][0]

        if new_offset < 3 and bucket_start == 0:
            if new_offset == offset:
                data_list[temp] = initial_list[new_offset-1]





        offset = new_offset - bucket_start

        #bucket_end = boundry_list[element_count-1-temp][1]

    return  data_list



def getkthelementrecursive(k,array=None):
    global initial_list
    if k < 4 :
        if array is not None:
            array[-1] = initial_list[k-1]
            return  array
        return [initial_list[k-1]]
    num = bucket_start= j= num_trail = 3
    element_count=1

    while j < k:
        num_trail = num
        bucket_start = j
        num = num * 3
        j += (num)
        bucket_end = j
        element_count+=1

    offset = k - bucket_start
#    print offset
    data_list = [2] * element_count
    if array is not None:
        array[len(array)-element_count]= initial_list[ ((offset-1)/num_trail) ]
        data_list = array
    else:
        data_list[0] = initial_list[ ((offset-1)/num_trail) ]
    #print data_list
    # if array is not None:
    #     data_list = mergelist(array,data_list)
    #print data_list

    #print "start : %s | end : %s | length : %s | bucket offset %s %s"%(bucket_start,bucket_end,element_count,offset,num_trail)
    new_offset=  (bucket_start - num_trail) + ( offset - ((num_trail)*((offset-1)/num_trail)))

    return getkthelementrecursive(new_offset,data_list)











    #return getkthelementrecursive(offset)

def getkthelement(k):
    j = 3
    num = 3
    element_count = 2

    while j < k:
        num = num * 3

        j += num
        element_count += 1
    #print element_count
    #print j
    left = j - k


    left_item = element_count -2
    list = [4] * element_count
    while left > 0:
        temp_left_item = left_item

        while temp_left_item >= 0:
            if list[temp_left_item] > 2:
                break
            else:
                temp_left_item -= 1

        list[temp_left_item] -= 1

        p = temp_left_item + 1

        while p <= left_item:
            list[p] = 4
            p+=1
        left -= 1
        #print list
    item =0
    # while item < len(list)-1:
    #     print list[item],
    #     item+=1
    # print ""
    return list[0:-1]

# print getkthelementrecursive(29)
# print getkthElementIterative(29)

#tests=int(raw_input())

# while  tests > 0:
#     t=int(raw_input())
#     getkthelement(t)
#     tests-=1
# getkthelement(29)
# print getkthelementrecursive(29)
# getkthelement(21)

yappi.start()
#
count=9999999
number=count
while number > 0:
    #getkthelementrecursive(number)
    getkthElementIterative(number)
    #getkthelement(number)
    number-=1
    #print number
#yappi.get_func_stats().print_all()

# yappi.stop()
# yappi.start()
#
# number=count
# while number > 0:
#     #getkthelementrecursive(number)
#     getkthElementIterative(number)
#     #getkthelement(number)
#     number-=1
#     #print number
yappi.get_func_stats().print_all()
temp =0
# while temp < number:
#
#     try:
#         first_result = getkthElementIterative(temp)
#         second_result = getkthelementrecursive(temp)
#
#         if first_result != second_result:
#             print " number : %s , first_result: %s second_result: %s"%(temp,first_result,second_result)
#     except Exception as e:
#         print "error in number %s , %s "%(temp, e)
#     temp+=1




# print getkthelement(21)
# print getkthelementrecursive(21)
# getkthelement(141)
# getkthelementrecursiveDriver(141)
# getkthelement(119)
# getkthelementrecursiveDriver(119)
# getkthelement(30)
# getkthelementrecursiveDriver(30)
# getkthelement(6)
# getkthelementrecursiveDriver(6)







# ********************
# tests=int(raw_input())
# #print tests
# while  tests > 0:
# t=int(raw_input())
# 	#print t
# 	result = t
# 	initial_list=[2,3,4]
# 	new_list=[]
# 	new_list.extend(initial_list)
# 	condition= true
# 	final_list=[2,3,4]
# 	while t >= 1:
# 		temp_list=[]
# 		for i in initial_list:		

# 			for data in new_list:
# 				new_str="%s%s"%(i,data)
# 				temp_list.append(new_str)
# 				# print new_str,
# 		#print new_list		
# 		new_list=temp_list
# 		final_list.extend(new_list)
# 		if len(new_list) > t:
# 			condition = false
# 			#print 'breaking'
# 			break
# 		t-= 1
# 	#print len(final_list)
# 	#print final_list

# 	print final_list[result-1]

# 	tests-=1






