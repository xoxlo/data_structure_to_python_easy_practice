from training_9_10 import *
from training_9_11_14 import *

def insert_avl(root, node):
    if root == None:
        return node
    
    if node.key == root.key:
        return root
    
    if node.key < root.key:
        root.left = insert_avl(root.left, node)
    elif node.key > root.key:
        root.right = insert_avl(root.right, node)
    
    bf = calc_height_diff(root)
    
    if bf > 1:
        if node.key < root.left.key:
            return rotateLL(root)
        else:
            return rotateLR(root)
        
    elif bf < -1:
        if node.key < root.right.key:
            return rotateRL(root)
        else:
            return rotateRR(root)
        
    return root