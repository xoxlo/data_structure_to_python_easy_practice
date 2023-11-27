def search_max_bst(n): # 최대 값의 노드 탐색
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n): # 최소 값의 노드 탐색
    while n != None and n.left != None:
        n = n.left
    return n