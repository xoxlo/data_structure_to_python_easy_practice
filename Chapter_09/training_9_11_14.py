def rotateLL(A): # AVL트리의 LL회전
    B = A.left # 시계 방향 회전
    A.left = B.right
    B.right = A
    return B

def rotateRR(A): # AVL트리의 RR회전
    B = A.right # 반시계 방향 회전
    A.right = B.left
    B.left = A
    return B

def rotateRL(A): # AVL트리의 RL회전
    B = A.right
    A.right = rotateLL(B) # LL회전
    return rotateRR(A) # RR 회전

def rotateLR(A): # AVL트리의 LR회전
    B = A.left
    A.left = rotateRR(B) # RR회전
    return rotateLL(A) # LL회전