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