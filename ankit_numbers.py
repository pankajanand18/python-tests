n=1


import copy

def ankitSum(target,data,sum_total):
	#print data
	for i in xrange(len(data)):
		new_target = list(target)
		new_data = list(data)
		new_target.append(data[i])
		new_data = data[i+1:]
		#print new_target
		sum_total = sum_total + sum(new_target)

		sum_total = ankitSum(new_target,new_data,sum_total)
	#print sum_total
	return sum_total




# def getSum(n,t):
# 	sum = 0
# 	for i in xrange(1,t+1):
# 		print i
# 		for j in xrange(1,t+1):
# 			sum += j
# 	return sum

t=input()

for i in xrange(t):
	n=input()
	target=[]
	data= range(1,n+1)	
	print ankitSum(target,data,0)
