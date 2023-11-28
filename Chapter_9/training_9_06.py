from training_9_05 import *

def insert_bst(root, node):
    if root == None:
        return node
    
    if node.key == root.key:
        return root
    
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)
    
    return root

def delete_bst(root, key):
    if root == None:
        return root
    
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    else:
        if root.left == None:
            return root.right
        if root.right == None:
            return root.left
        
        succ == search_min_bst(root.right)
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)
    