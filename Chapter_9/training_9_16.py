from training_9_01 import *
from training_9_02 import *
from 

node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
root = None
for i in node:
    n = BSTNode(i)
    root = insert_avl(root, n)
    
    print("BST(%d): ",%i, end='')
    levelorder(root)
    print()
    
    print(" 노드의 개수 = ",count_node(root))
    print(" 단말의 개수 = ",count_leaf(root))
    print(" 트리의 높이 = ",calc_height(root))