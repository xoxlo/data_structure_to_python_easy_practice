from training_9_01 import *
from training_9_02 import *
from 

node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
root = None
for i in node:
    n = BSTNode(i)
    root = insert_avl(root, n)