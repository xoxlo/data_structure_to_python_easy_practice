from training_9_01 import * # BSTNode 생성 모듈 불러오기
from training_9_02 import * # 이진탐색트리 탐색 모듈 불러오기
from training_9_15 import * # AVL트리 삽입 모듈 불러오기
from CircularQueue_levelorder import *

def calc_height(n): # 이진트리의 높이 계산 함수
    if n is None: # 공백 트리 -> 0 반환
        return 0
    hLeft = calc_height(n.left) # 왼쪽트리의 높이
    hRight = calc_height(n.right) # 오른쪽트리의 높이
    if (hLeft > hRight): # 높이는 좌,우 어느 곳이든 상관없으니까 더 높은 트리에다가 +1을 해주면서 반환
        return hLeft + 1
    else:
        return hRight + 1

def count_node(n): # 순환을 이용해 트리의 노드 수 계산하는 함수
    if n is None: # n이 None이면 공백트리, 0을 반환
        return 0
    else: # 좌우 서브트리의 노드 수의 합 + 1을 반환
        return 1 + count_node(n.left) + count_node(n.right)
    
def count_leaf(n): # 단말 노드 수 계산 함수
    if n is None: # 공백트리 -> 0 반환
        return 0
    elif n.left is None and n.right is None: # 단말노드 -> 1 반환
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right) # 비단말 노드 -> 좌 + 우 결과 합
    
node = [0,1,2,3,4,5,6,7,8,9]
root = None
for i in node:
    n = BSTNode(i)
    root = insert_avl(root, n)

    
    print("BST(%d): "%i, end='')
    levelorder(root)
    print()
    
    print(" 노드의 개수 = ",count_node(root))
    print(" 단말의 개수 = ",count_leaf(root))
    print(" 트리의 높이 = ",calc_height(root))