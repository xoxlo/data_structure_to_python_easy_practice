from training_8_01 import TNode
from training_8_02_4 import inorder, postorder, preorder
from training_8_05 import CircularQueue, levelorder
from training_8_06_7 import count_leaf, count_node
from training_8_08 import calc_height

d = TNode('D',None,None) # D 삽입, 자식 없음
e = TNode('F',None,None)
b = TNode('B',d,e) # B 삽입, 왼쪽 자식 -> d, 오른쪽 자식 -> e
f = TNode('F',None,None)
c = TNode('C',f,None) # C 삽입, 왼쪽 자식 -> f, 오른쪽 자식 -> 없음
root = TNode('A',b,e) # 루트 노드에 A 삽입, 왼쪽 자식 -> b, 오른쪽 자식 -> c

    
print('\nIn-Order    : ', end='') # 중위 순회 ( LVR )
inorder(root)
print('\nPre-Order   : ', end='') # 전위 순회 ( VLR )
preorder(root)
print('\nPost-Order  : ', end='') # 후위 순회 ( LRV )
postorder(root)
print('\nLevel-Order : ', end='') # 레벨 순회
levelorder(root)
print()

print("노드의 개수 = %d개" % count_node(root))
print("단말의 개수 = %d개" % count_leaf(root))
print("트리의 높이 = %d" % calc_height(root))