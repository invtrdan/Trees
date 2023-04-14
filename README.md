# Trees
In Python, trees are a non-linear data strucutre that represents a hierarchial structure with nodes connected by edges. Trees are widely used in computer science and programming for tasks such as representing hierarchial relationships, searching and sorting algorithms, and parsing expressions.\

Here are some key concepts related to trees in Python:
1. Node: A node is a fundamental unit in a tree that contains data and zero or more child nodes. In Python, a node in a tree can be represented as an object or a dictionary with attributes, or even a simple class.
2. Root: The root of a tree is the topmost node in the tree that does not have any parent node. It serves as the entry point for accessing the entire tree. 
3. Children: Children are the nodes that are directly connected to a parent node. In a tree, a node can have zero or more children.
4. Parent: A parent is a node that has one or more child nodes connected to it. Except for the root node, every node in a tree has exactly one parent.
5. Leaf: A leaf node, also known as a terminal node or a leaf, is a node that does not have any children. It is the end point of a tree branch.
6. Subtree: A subtree is a portion of a tree that can be viewed as a complete tree by itself. It consists of a node and its descendants.
7. Depth: The depth of a node in a tree is the length of the path from the root to that node. The root has a depth of 0, its children have a depth of 1, and so on.
8. Binary Tree: A binary tree is a tree in which each node has at most two children. it is one of the most commom types of trees used in computer science and programming.
9. Tree Traversal: Tree traversal refers to the process of visiting and processing all the nodes in a tree in a specific order. Common tree traversal algorithms in Python include in-order, pre-order, and post-order traversal.
10. Tree Operations: trees support various operations such as insertion, deletion, searching, and modification of nodes. These operations are essential for manipulating the data stored in a tree and maintaining its hierarchial structure.
11. A path is a sequence of 0 or more connected nodes. 
* The length of a path is the number of edges in the path.
* The depth of a node is the number of edges on the path from the root to the node.
* The height of a tree is the number of edges on the longest path from the root to a leaf node.  
12. Ancestor: Node A is an ancestor of Node B if there exists a path from A to B.
13. Descendant: Node B is a descendant of Node A if there exists a path from A to B. 

Python provides built-in data structures such as lists and dictionaries that can be used to implement trees. Additionally, there are third-party libraries such as "binarytree" and "treelib" that provide pre-implemented tree data structures and algorithms for easy use in Python programs.\

Q: How many branches are in a tree with N nodes?\
A: n-1\
Q: What is the height and depth of an empty tree?\
A: -1 

## Tree Traversals

A tree traversal is an algorithm that steps through every node in a tree in some order. 

Level 1       A        height = 2
             / \
Level 2     B   C      height = 1
           / \
Level 3   D   E        height = 0

### Preorder Traversal
* Visit the root
* Traversel Left
* Traverse Right

A -> B -> D -> E -> c

### Inorder Traversal
* Traverse Left
* Visit the root
* Traverse Right

D -> B -> E -> A -> C 

### Postorder Traversal
* Traverse Left
* Traverse Right
* Visit Root

D -> E -> B -> C -> A

### Level Order Traversal

## Binary Trees

Binary trees are a type of tree data structure where each node has at most two children. These children are typically referred to as the left child and the right child. A binary tree is a hierarchical structure where nodes are organized in levels, starting from the root node at level 0 and moving downward to leaf nodes at the deepest level.\

Binary trees have a few key properties:

* Root: The topmost node in the binary tree is called the root. It serves as the starting point for traversing the tree.
* Nodes: Each node in the binary tree contains a value or data, and can have at most two child nodes.
* Left Child and Right Child: Each node can have a left child and/or a right child, which are its immediate descendants in the tree. The left child is typically smaller (or equal) in value compared to the parent node, while the right child is larger (or equal).
* Leaf Nodes: Leaf nodes are the nodes that do not have any children. They are also referred to as terminal nodes, as they represent the end of a branch in the tree.
* Binary trees can be used to represent a wide variety of data structures, such as search trees, expression trees, and decision trees. They can be used for tasks such as searching, insertion, deletion, and traversal of data in an efficient manner.
* Each Node must have no more than 2 vhildren.

There are various types of binary trees, including binary search trees, AVL trees, red-black trees, and heap trees, each with their own specific rules and properties. Binary trees are widely used in computer science and programming due to their efficiency and versatility in representing and processing data in a hierarchical manner.\

### Types of Binary Trees

#### Full Tree
* Every node has 0 or 2 children

  A

  A\
 / \\
B   C\
   / \\
  D   E

#### Complex Tree
* All levels are completely filled, except possibly the last, which is filled from left to right.

   A

   A\
  / \\
 B   C\
/ \ / \\
C D E  F