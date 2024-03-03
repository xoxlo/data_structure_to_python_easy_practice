def search_bst_iter(n, key): # 이진탐색트리의 탐색 ( 반복 )
    while n != None: # n이 None이 아닐 때 까지 반복
        if key == n.key: # n의 키 값이 찾는 키값과 동일 -> 탐색성공
            return n # n 반환
        elif key < n.key: # n의 키값이 찾는 키값보다 더 작을 때
            n = n.left # n을 왼쪽 서브트리의 루트로 이동 -> 탐색
        else: # n의 키값이 찾는 키값보다 더 클 때
            n = n.right # n을 오른쪽 서브트리의 루트로 이동 -> 탐색
    return None # 없으면 찾는 키의 노드 X