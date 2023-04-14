'''
Write a method that receives the root of a binary tree and 
returns the sum of all the values stored in it.

* Preorder Traversal
'''

def sum_all(root):
    # Base Case: Empty Tree
    if not root:
        return 0
    return root.val + sum_all(root.left) + sum_all(root.right)


