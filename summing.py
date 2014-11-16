


def getSum(list,start_index,end_index):
	return sum(list[start_index:end_index+1])


# print getSum([0,1, 2, 3, 4, 5],1,2)
# print getSum([0,1, 2, 3, 4, 5],1,3)
# print getSum([0,1, 2, 3, 4, 5],2,3)
# print getSum([0,1, 2, 3, 4, 5],3,4)

input_array=[0]
array_size=input()
input_data = raw_input()
input_array=[int(i) for i in input_data.split(' ')]

test_cases= input()
input_size=[]
for i in xrange(test_cases):

	start = raw_input()
	actual_data= start.split(' ')	
	input_size.append((actual_data[0],actual_data[1]))

for data in input_size:
	print getSum(input_array, data[0],data[1])