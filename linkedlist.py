from pyclbr import Class


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.value=new_node.value
        self.head=new_node
        self.tail=new_node
        self.length=1
    def append(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode   
        else:
            self.tail.next=newnode
            self.tail=newnode
        self.length+=1
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

newlinkedlist=LinkedList(5)
newlinkedlist.printlist()
newlinkedlist.append(10)
newlinkedlist.printlist()
    