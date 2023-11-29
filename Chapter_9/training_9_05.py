def search_max_bst(n): # 최대 값의 노드 탐색 - 반복
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n): # 최소 값의 노드 탐색 - 반복
    while n != None and n.left != None:
        n = n.left
    return n

# def search_max_bst(n): # 최대 값의 노드 탐색 - 순환
#    while n != None and n.right != None:
#        n = search_max_bst(n.right)
#    return n

# def search_min_bst(n): # 최소 값의 노드 탐색 - 순환
#    while n != None and n.left != None:
#        n = search_min_bst(n.left)
#    return n