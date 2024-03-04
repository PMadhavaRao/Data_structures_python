# Initialise the Node
class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.item = data
        self.next = None
        self.prev = None
# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.head= None
#traversal or printin
def print(self):
    if self.head is None:
        print("dll is empty");
        return
    itr=self.head
    dllstr=""
    while itr:
        dllstr+=str(itr.data)+'-->'
        itr=itr.next
    print(dllstr)
def insert_at_begin(self,data):
    if self.head is None:
        new_node=Node(data)
        self.head=new_node
    else:
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.head.prev=new_node
        
insert_at_begin(10)
    
   
