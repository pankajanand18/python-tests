def generator():
	mylist = range(5)
	for i in mylist:
		yield i*i


gen = generator()
for i in gen:
	print " start"
	print i 