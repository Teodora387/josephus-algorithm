class Node:         #create the class Node which is essential for building the cicular linked list
    def __init__(self, val):
        self.val=val
        self.next=None

class CircularList:     #build a ciruclar linked list because in the problem, the persons are sitting in a circle
    def __init__(self):
        self.first=None

    def append(self, val):      #put a new value in a new node at the end of the list
        node=Node(val)
        self.putAtEnd(node)

    def getNode(self, index, start):     #get the position of a node. this function is useful for constructing the next function, previous node
        if self.first is None:
            returnNone
        current=start
        for i in range(index):
            current = current.next
        return current

    def prevNode(self, referenceNode):      #this function helps us to build the function putBefore because, for inserting a new node in front of another, we need to know which is the previous node
        if self.first is None:              #the variable from the function's argument, referenceNode, it is an arbitrary node that we take as a reference or guide
            return None
        current=self.first
        while current.next != referenceNode:
            current = current.next
        return current

    def putAfter(self, referenceNode, newNode):     #puts a new node after another one
        newNode.next = referenceNode.next
        referenceNode.next = newNode

    def putBefore(self, referenceNode, newNode):    #puts a new node before another one
        previous = self.prevNode(referenceNode)
        self.putAfter(previous, newNode)            #putBefore is made as a putAfter function: it inserts a node after the previous node of the referenceNode

    def putAtEnd(self, newNode):                    #appends a node
        if self.first is None:                      #if the head is NULL, the new node is set as head
            self.first = newNode
            newNode.next = newNode
        else:
            self.putBefore(self.first, newNode)     #if the head is not NULL, we use the putBefore function, wich uses the putAfter function for inserting anew node at the end of the list

    def delete(self, node):     #function for deleting a node
        if self.first.next == self.first:
            self.first = None
        else:
            previous = self.prevNode(node)
            previous.next = node.next
            if self.first == node:
                self.first = node.next

    def verify(self, val):      #function to check if a value is in the list. This function is useful when we search for the third 
        node = self.first
        while node.next != self.first:
            if node.val is val:
                return True
            node = node.next
        if node.val is val:     #to check for the last element
            return True
        return False

    def thirdElement(self, val):        #list the third element 
        if self.verify(val):
            node = self.first
            while node.val != val:
                node = node.next
            return node.next.next.next.val


def oneNode(cList):         #function to check if the list has only one node
    if cList.first.next == cList.first:
        return True
    else:
        return False

def josephuSolution(cList, k):      #the actually solution for the problem 
    if cList.first is None:         #if the list is empty, we return none
        return None
    start = cList.first         #start going through the list starting with the first node
    while not oneNode(cList):       #while the list has more the 1 node 
        toRemove = cList.getNode(k-1, start)    #we get the position of the node we need to remove
        start = toRemove.next       #set the node we will remove
        cList.delete(toRemove)      #delete that node
    return cList.first.val          

a_cList = CircularList()
n=int(input("Input the number of people: "))
k=int(input("Choose a number: "))
for i in range(1, n+1):     #create the list from 1 to n+1
    a_cList.append(i)

ans=josephuSolution(a_cList, k)     #apply the function to see which is the last node or who is the last person alive
print('The last person alive is {}'.format(ans))