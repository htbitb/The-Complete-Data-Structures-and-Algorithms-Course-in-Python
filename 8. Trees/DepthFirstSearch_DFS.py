from Tree import Binary_Tree, Node

class Traversal(Binary_Tree):
    def DFS_Preorder(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
    def DFS_PostOrder(self):
        result  = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result
    
    def DFS_InOrder(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
a = Traversal()
a.Insert(45)
a.Insert(34)
a.Insert(36)
a.Insert(90)
a.Insert(58)
a.Insert(47)
print(a.DFS_PostOrder())
