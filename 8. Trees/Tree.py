class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Binary_Tree:
    def __init__(self):
        self.root = None
        
    def Insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
    
    def Contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.leff
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
