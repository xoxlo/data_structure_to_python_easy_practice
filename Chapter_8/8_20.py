def level(root, node): # 레벨 구하는 함수 - 재귀함수 이용
    if root is None: # 루트 노드가 None이면
        return 0 # 0 반환

    if root == node: # 루트노드와 같다면
        return 1 # 1 반환

    left_level = level(root.left, node)
    
    if left_level is not None: # 왼쪽 자식이 비어있지 않다면
        return left_level + 1 # +1해서 반환

    right_level = level(root.right, node)
    
    if right_level is not None: # 오른쪽 자식이 비어있지 않다면
        return right_level + 1 # +1해서 반환
    
    