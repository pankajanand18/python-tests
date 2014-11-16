from guppy import hpy
num=10000
#mygenerator = (x*x for x in range(num))
mygenerator = [x*x for x in range(num)]


for i in mygenerator:
	print(i)

h = hpy()
print h.heap()
