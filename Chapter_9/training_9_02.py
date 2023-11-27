def search_bst(n, key): # 이진탐색트리의 탐색 ( 순환 구조 )
    if n == None:
        return None
    elif key == n.key: # n의 키값과 동일 -> 탐색 성공
        return n
    elif key < n.key: # n의 키 값보다 찾는 키값이 더 작을 때
        return search_bst(n.left, key) # 왼쪽 서브트리에서 탐색
    else: # n의 키 값보다 찾는 키값이 더 클 때
        return search_bst(n.right, key) # 오른쪽 서브트리에서 탐색