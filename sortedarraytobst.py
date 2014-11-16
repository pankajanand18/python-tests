class TreeNode:
	def __init__(self):
		self.right = None
		self.left= None
		self. data= None
	def __str__(self):
		return "%s"%self.data

	



def preorder(root):
	if root is None or root.data is None:
		return
	
	preorder(root.left)
	print root.data
	preorder(root.right)


def createBst(list,start,end):

	if start > end: 
		return None

	root = TreeNode()
	mid = (start+end)/2	
	root.data = list[mid]
	
	

	root.left = createBst(list,start,mid-1)
	root.right = createBst ( list,mid+1,end)
	return root

list=[1,2,3,4,5,6,7,8,9]

root = createBst(list,0,len(list)-1)
print preorder(root)