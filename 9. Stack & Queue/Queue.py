class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    def __inti__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def Enqueue(self, value):
        new_node = Node(value)
        self.last.next = new_node
        self.last = new_node
        self.length += 1
    
    def Dequeue(self):
        if self.first is None:
            print("the queue is empty")
        else:
            temp = self.first
            self.first = self.first.next
            self.length -= 1
            temp.next = None
            return temp.value

