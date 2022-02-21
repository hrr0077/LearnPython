# Node class

class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data #Assign data
        self.next = None # Initialize next as Null

class LinkedList:
    # Function to initialize the Linked
    # List Object
    def __init__(self):
        self.head = None
    
# Code Executes from here

if _name_ =='_main_':

    # Start with the empty List
    llist = LinkedList()

    llist.head = Node(1)
    secound = Node(2)
    third = Node(3)

    llist.head.next = secound
    llist.next = third
