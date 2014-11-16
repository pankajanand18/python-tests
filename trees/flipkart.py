from collections import deque
__author__ = 'pankaj'

# class to hold the Tree's Nodes Structure
class Tree(object):
    def __init__(self,data,left,right):
        self.left = left
        self.right = right
        self.data = data
    def __str__(self):
    	return "[Data : %s, R : %s, L %s]"%(self.data,self.right,self.left)





# function to build the tree with given input array with each element point to its root
def buildTree(input):
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
    return root_node




#function to print the tree in reverse level order traversal
def printReverseOrder(root_node):
    queue=deque()
    queue.append(root_node) # Insert Root node first
    stack=[]

    # this will create an stack with boundary of levels marked as None Items in stack
    while True:
        nodeCount = len(queue)
        if nodeCount == 0:
            break
        stack.append(None)
        while nodeCount > 0:
            node = queue.popleft()
            stack.append(node.data)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            nodeCount-=1


    dup_stack=[]
    while len(stack) > 0:
        item = stack.pop()
        if item == None:
            # Once the boundary is found reverse the found elements and print
            dup_stack.reverse()
            for i in dup_stack:
                print '%s'%(i),
            print ''
            dup_stack=[]
        else:
            # As we are reading elements from the end keep it as it is to print in reverse form later on
            dup_stack.append(item)



total_nodes = int(raw_input())
temp = 0
nodes = raw_input()
nodes = nodes.split(' ')
node_list=[]
while temp < total_nodes:
    node_list.append(int(nodes[temp].strip()))
    temp+=1

root_node=buildTree(node_list)
printReverseOrder(root_node)








