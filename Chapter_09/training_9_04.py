def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value: # 찾으려는 value와 n의 value와 동일 --> 탐색 성공
        return n # n 반환 ( 루트 노드 )
    res = search_value_bst(n.left, value) # 왼쪽 서브트리에서 탐색
    if res is not None: # 탐색 성공 ( res가 not None )
        return res # res 반환
    else:
        return search_value_bst(n.right, value) # 오른쪽 서브트리에서  탐색