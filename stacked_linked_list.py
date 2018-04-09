#My clss for creating nodes for my linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Defining the class which will create my linked list
class LinkedList:
    def __init__(self):
        self.root = None

# Method to check if stack is empty
    def isEmpty(self):
        return True if self.root is None else False

# Method to push items to the stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node
        print(str(data) + " successfully pushed to stack")

# Method to pop items from the stack
    def pop(self):
        if self.isEmpty():
            print("The Stack is empty now")
            return
        popped = self.root.data
        self.root = self.root.next
        print("The value removed is: " + str(popped))
    
    def print(self):
        while Node.next != None:
            print(x)
        

#Testing my functions to see if they work.

# Creating our stack in form of linked list
stack = LinkedList()

# Pushing values in stack
stack.push(10)              
stack.push(20)
stack.push(30)

# Poping values from stack
stack.pop()                 
stack.pop()
stack.pop()
stack.pop()
    