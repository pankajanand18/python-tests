

from linkedlist import SinglyLinkedListNode




def reverseList(head):

    tail=None
    last=None
    tempNode = head
    while tempNode is not None:
        currentNode, tempNode = tempNode, tempNode.next
        currentNode.next = tail
        tail = currentNode


    return tail

def reverseListKNode(head,k):
    tempHead= None
    tempTail= None
    while head is not None:
        tempNode = head
        last = None
        tk=k
        while tempNode is not None and tk > 0:
            currentNode,nextNode = tempNode,tempNode.next
            currentNode.next = last
            last=currentNode
            tempNode = nextNode
            tk-=1
        if tempHead is not None:
            tempTail.next = last
            head.next = nextNode
        else:
            tempHead = last
            head.next= nextNode


        tempTail =  head
        head=nextNode

    return  tempHead













def printLinkedList(head):

    while head is not None:
        print head.data,
        head=head.next
    print ''





def createList(list):

    lastNode=None
    head=None
    for i in list:
        node= SinglyLinkedListNode(i)
        if lastNode == None:
            lastNode = node
            head = node
        else:
            lastNode.next = node
            lastNode=node

    return head


a=(i for i in xrange(1,11))
list = createList(a)
printLinkedList(list)
newList=reverseListKNode(list,2)
printLinkedList(newList)



