
a='Mahendra   Singh  Dhoni'
aStriped = a.split(' ');
length = len(aStriped)
newString=[]
for i in xrange(0,length):
	if len(aStriped[i].strip())>0:
		if i < length-1:
			newString.append(aStriped[i][0])
		else:
			newString.append(aStriped[i])

print " ".join(newString)
