<!-- Heading -->
## What is Binary Trees?
A Binary Tree is a type of tree data structure where each node can have a maximum of two child nodes, a left childe node and a right childe node.

This restriction, that a node can have a maximum of two child nodes, gives us many benefits:
* Algorithms like traversing, searching, insertion and deletion become easier to understand, to implement, and run faster.
* Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
* Balancing trees is easier to do with a limited number of child nodes, using an AVL Binary Tree for example.
* Binary Trees can be represented as arrays, making the tree more memory efficient.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOzKWtBvrCt-we6eV4ox3qVHd31NPvAykhYX-iRomhYw&s)

## Binary Trees vs Arrays and Linked Lists
* **Arrays** are fast when you want to access an element directly, like element number 700 in an array of 1000 elements for example. But inserting and deleting elements require other elements to shift in memory to make place for the new element, or to take the deleted elements place, and that is time consuming.
  

* **Linked Lists** are fast when inserting or deleting nodes, no memory shifting needed, but to access an element inside the list, the list must be traversed, and that takes time.


* [**Binary Trees**](Tree.py), such as Binary Search Trees and AVL Trees, are great compared to Arrays and Linked Lists because they are BOTH fast at accessing a node, AND fast when it comes to deleting or inserting a node, with no shifts in memory needed.


## Binary Tree Traversal
* [**Breadth First Search (BFS)**](BreadthFirstSearch.py) is when the nodes on the same level are visited before going tto the next level in the tree. This means that the tree is explored in a more sideways direction.

* [**Depth First Search (DFS)**](DepthFirstSearch_DFS.py) is when the traversal moves down the tree all the way to the leaf nodes, exploring the tree branch by branch in a downwards direction.