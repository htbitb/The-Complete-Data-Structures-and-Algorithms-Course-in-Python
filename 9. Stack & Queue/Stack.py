# Create stack with linked lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
# Print each element of the stack        
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp  = temp.next
# insert new value into the     
    def Push(self, value):
        if self.top is None:
            new_node = Node(value)
            self.top = new_node
            self.height = 1
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
            self.height += 1
# delete and return the top element    
    def Pop(self):
        current_node = self.top
        self.top = self.top.next
        current_node.next = None
        self.height -= 1
        return current_node.value

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    
    def Size(self):
        return self.height

