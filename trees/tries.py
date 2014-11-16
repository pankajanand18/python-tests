__author__ = 'pankaj'

class TriesNode:
    object_count =0
    def __init__(self):
        self.data = None
        self.links={}
        TriesNode.object_count+=1

    def getObjectCount(self):
        return TriesNode.object_count


def newFun():
    print 'hello world '

node = TriesNode()
node.getSize = newFun
node.object_count =5

node.getSize()
node1 = TriesNode()
print node.getObjectCount()



