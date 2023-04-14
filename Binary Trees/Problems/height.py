'''
Write a method that receives the root of a binary tree and returns the tree's height.

Time Complexity:
Space COmplexity:
'''
from treenode import *

def get_height(root: TreeNode) -> int:
    if not root: return -1
    return 1 + max(get_height(root.left, get_height(root.right)))








def height_of_tree(root: TreeNode) -> int:
    if root is None:  # Base case: an empty tree has height 0
        return 0
    else:
        left_height = height_of_tree(node.left)  # Recursively calculate left subtree height
        right_height = height_of_tree(node.right)  # Recursively calculate right subtree height
        return max(left_height, right_height) + 1  # Height is the maximum of left and right subtree heights, plus 1 for the current level



from collections import deque

def height_of_tree(root: TreeNode) -> int:
    if root is None:  # Base case: an empty tree has height 0
        return 0

    queue = deque([(root, 0)])  # Initialize a queue with root node and its level
    height = 0  # Initialize height to 0

    while queue:
        node, level = queue.popleft()  # Dequeue a node and its level
        height = max(height, level)  # Update height with the current level
        if node.left:  # If left child exists, enqueue it with its level incremented by 1
            queue.append((node.left, level + 1))
        if node.right:  # If right child exists, enqueue it with its level incremented by 1
            queue.append((node.right, level + 1))

    return height

