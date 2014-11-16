from fractions import gcd

def getIntegerInput():
	inputs = raw_input()
	input_int_list=[]
	global original_numbers

	for data in inputs.split(' '):
		data = int(data)
		input_int_list.append(data)
		
	#print input_int_list
	return input_int_list


t_str = raw_input()
t= int(t_str)
original_numbers = range(1,t+1)
inputs = raw_input()


item_found= None

for data in inputs.split(' '):
	data = int(data)	
	if original_numbers[data-1] > data:
		item_found = data
		break
	else:
		original_numbers[data-1] = data + 1 


#print item_found
# for i in xrange(0,t):
# 	if original_numbers[i] == i+1:
# 		missing_found = i+ 1
# 		break

original_numbers = range(1,t+1)	


#original_numbers.remove(missing_found)

#print missing_found
#print item_found

print item_found,

for i in original_numbers:	
		print i,


