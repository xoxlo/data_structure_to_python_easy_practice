from training_8_01 import TNode
from training_8_02_4 import inorder, postorder, preorder
from training_8_05 import CircularQueue, levelorder
from training_8_06_7 import count_leaf, count_node
from training_8_08 import calc_height
d = TNode('D',None,None)
e = TNode('E',None,None)
b = TNode('B',d,e)
f = TNode('F',None,None)
c = TNode('C',f,None)
root = TNode('A',b,c)


print('\nIn-Order    : ', end='')
inorder(root)
print('\nPre-Order   : ', end='')
preorder(root)
print('\nPost-Order  : ', end='')
postorder(root)
print('\nLevel-Order : ', end='')
levelorder(root)
print()

print("노드의 개수 = %d개" % count_node(root))
print("단말의 개수 = %d개" % count_leaf(root))
print("트리의 높이 = %d" % calc_height(root))