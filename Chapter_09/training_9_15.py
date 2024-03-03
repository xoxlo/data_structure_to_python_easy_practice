from training_9_10 import *
from training_9_11_14 import *

def insert_avl(root, node): # AVL 트리의 삽입 연산
    if root == None: # 공백 노드 -> 이 위치에 삽입
        return node # 노드를 반환 ( 이 노드가 현개 root 위치에 감 )
    
    if node.key == root.key: # 동일한 키는 허용 X
        return root # root를 반환
    
    if node.key < root.key: # 추가하려는 키가 root의 key보다 작으면
        root.left = insert_avl(root.left, node) # 왼쪽 서브트리로 진행
    elif node.key > root.key: # 추가하려는 키가 root의 key보다 크면
        root.right = insert_avl(root.right, node) # 오른쪽 서브트리로 진행
    
    bf = calc_height_diff(root) # bf - 균형인수(balance factor) -> lh(왼쪽높이) - rh(오른쪽높이)
    
    if bf > 1: # 왼쪽 서브트리에서 불균형 발생 -> LL or LR
        if node.key < root.left.key: # 왼쪽 -> 왼쪽에 삽입 : LL
            return rotateLL(root)
        else:                        # 왼쪽 -> 오른쪽에 삽입 : LR
            return rotateLR(root)
        
    elif bf < -1: # 오른쪽 서브트리에서 불균형 발생 --> RR or RL
        
        if node.key < root.right.key:  # 오른쪽 -> 왼쪽에 삽입 : RL
            return rotateRL(root)    
        else:                          # 오른쪽 -> 오른쪽에 삽입 : RR
            return rotateRR(root)
        
    return root