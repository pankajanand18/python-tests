__author__ = 'pankaj'


class HeapNode(object):
    def __init__(self,data):
        self.data= data
        self.count = 0
        self.nodeLocation = None


class Heap(object):
    capacity=10
    def __init__(self):
        self.nodes=[None] * (Heap.capacity+1)
        self.size= 1

    def maxHeapify(self,index):

        # do heapify here
        left = 2 * index
        right = 2 * index + 1
        largest = index
        if left <= self.size and self.nodes[left].count > self.nodes[largest].count:
            largest = left
        if right <= self.size and self.nodes[right].count > self.nodes[largest].count:
            largest = right

        if largest is not index:
            tempNode = self.nodes[largest]
            self.nodes[largest] = self.nodes[index]
            self.nodes[index] = tempNode
            self.nodes[index].nodeLocation.minHeapLoc = index
            self.nodes[largest].nodeLocation.minHeapLoc = largest
            self.maxHeapify(largest)

    def getElement(self,index):
        return self.nodes[index]

    def insertElement(self,heapNode):

        if self.size < self.capacity:
            self.nodes[self.size] = heapNode
            self.size+=1
        elif self.size == self.capacity:
            # check leaf nodes
            size =self.size -1
            while size > (self.size-1)/2 :
                if self.nodes[size].count < heapNode.count:
                    self.nodes[size] = heapNode
                    self.maxHeapify(size)
                    break
                size-=1



class Tries(object):
    max_nodes= 26;
    def __init__(self,rootNode=False):
        self.nodes=[None]*Tries.max_nodes # an array of 26 characters
        self.data=None
        self.leaf=False
        self.rootNode=rootNode
        self.minHeapLoc=-1

    def __str__(self):
        return self.data


    def populateNextElment(self,string):
        index=ord(string[0])-ord('a')
        node = self.nodes[index]
        if node == None:
            node = Tries()
            self.nodes[index] =node
        return node.insert_element(string)


    def insert_element(self,string):
        if self.rootNode == True:
            self.data=''
            return self.populateNextElment(string)


        if self.data==None:
            self.data= string[0]

        if len(string) == 1:
            self.leaf = True
            return self
        else:
            return self.populateNextElment(string[1:])

    def printAllString(self,string=None):
        if string is None:
            string=''

        if self.rootNode == False and self.leaf == True:
            print string+self.data
        i=0
        while i < Tries.max_nodes:
            node = self.nodes[i]
            if node is not None:
                node.printAllString('%s%s'%(string,self.data))
            i+=1

def insertIntoHeap(trieNode,heapRoot,data):
    if trieNode.minHeapLoc == -1:
        # No data inserted into Heap as of now
        heapNode = HeapNode()
        heapNode.data = data
        heapNode.nodeLocation = trieNode
        heapNode.count = 0

    else:
        heapNode= heapRoot.getElement(trieNode.minHeapLoc)
        heapNode.count += 1





heap=Heap()
rootNode=Tries(True)
rootNode.insert_element("a")
rootNode.insert_element("pankaj")
rootNode.insert_element("pankaja")
rootNode.insert_element("anand")
rootNode.insert_element("amand")
rootNode.printAllString('')









