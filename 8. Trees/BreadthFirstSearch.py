from Tree import Binary_Tree

class BreadthFirstSearch(Binary_Tree):    
    def BFS(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result


a = BreadthFirstSearch()
a.Insert(45)
a.Insert(34)
a.Insert(36)
a.Insert(90)
a.Insert(58)
a.Insert(47)
print(a.BFS())
