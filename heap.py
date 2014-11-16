a=[20,16,14,6,13,10,1,5,7,12,19]





def doHeapifyMax(list,i):
	print 'inside doHeapifyMax'
	right = 2 * i + 1 
	left = 2 * i + 2 ;
	largest = i
	length = len(list)
	if left < length and list[left] > list [ i]:
		largest = left
	if right < length and list[right] > list[i]:
		largest = right
	if largest != i:
		list[i], list[largest] = list[largest],list[i]	
		doHeapifyMax(list,largest)


def convertToHeap(list):
	length = len(list)
	for i in xrange(len(list)/2,-1,-1):
		print "%s : %s"%(i,length)
		doHeapifyMax(list,i)


def isMaxHeap(list):
	for i in range(0,len(list)/2):
		node = i 	
		if list[i] > list[(2*node)+1] and list [i] > list[(2*node)+2]:
			continue
		else:
			print 'not a max heap'
			print "%s %s %s"%(i,list[2*i+1],list[2*i+2])
			break
print a 
convertToHeap(a)
print a 
isMaxHeap(a)