# The node will be used to keep track of the items passed from the Queue
class Node:
    '''A node for a linked list.'''
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

#The Queue function will be used to pass data to the linked list.
class Queue(object):
    def __init__(self):
        self.head = None

    #The Enqueue function is used to add items to the linked list. 
    def enqueue(self, item):
        """Add an item onto the tail of the queue."""
        if self.head is None:
            self.head = Node(item)
            print("{0} has been added to the queue".format(item))
        else:
            current = self.head
            print("{0} has been added to the queue".format(item))
            while current.next is not None:
                current = current.next
            current.next = Node(item)
            
    #The Dnqueue function is used to remove items to the linked list. 
    def dequeue(self):
        if self.head is None:
            raise IndexError("Can't dequeue from empty queue.")
        else:
            first = self.head
            self.head = self.head.next
            print("{0} has been removed from the queue".format(first.data))
            return first.data


#This is my code to test my Node and Queue classes and their functions.
q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.dequeue()
q.dequeue()
q.dequeue()