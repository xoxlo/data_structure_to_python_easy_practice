class BSTNode: # 이진탐색트리를 위한 노드 클래스
    def __init__(self, key, value = None): # 생성자 ( 키와 값을 받음 )
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
def search_bst(n, key): # 이진탐색트리의 탐색 ( 순환 )
    if n == None:
        return None
    elif key == n.key: # n의 키값과 동일 -> 탐색 성공
        return n
    elif key < n.key: # n의 키 값보다 찾는 키값이 더 작을 때
        return search_bst(n.left, key) # 왼쪽 서브트리에서 탐색
    else: # n의 키 값보다 찾는 키값이 더 클 때
        return search_bst(n.right, key) # 오른쪽 서브트리에서 탐색