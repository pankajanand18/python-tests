class Tree(object):
    def __init__(self,data,left,right):
        self.left = left
        self.right = right
        self.data = data
    def __str__(self):
    	return "[Data : %s, R : %s, L %s]"%(self.data,self.right,self.left)



def getHeight(root_node):
	if root_node is None:
		return 0
	r_height= 1 + getHeight(root_node.right);
	l_height= 1 + getHeight(root_node.left)

	if r_height > l_height:
		return r_height
	else:
		return l_height
	
input=[1,5,5,2,2,-1,3]
hash={}
root_node=None
for i in xrange(len(input)):
	tree_node= Tree(i,None,None)
	hash.update({i:tree_node})


for i in xrange(len(input)):
	


	node = hash[i]
	if input[i] == -1:
		root_node = node
		continue

	parent = hash[input[i]]
	if parent.left is None:
		parent.left = node
	else:
		parent.right= node



	

# for item in hash.keys():
# 	print "%s : %s"%(item,hash[item])
print root_node
print getHeight(root_node)





