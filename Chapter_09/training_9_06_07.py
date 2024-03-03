from training_9_05 import * # 최대값, 최소값 노드 탐색 모듈 불러오기

def insert_bst(root, node): # 이진탐색트리의 삽입 연산
    if root == None: # root노드가 공백에 도달하면
        return node # node 삽입
    
    if node.key == root.key: # node키와 root키가 동일 하면 ? 이미 있으므로 허용 X
        return root # root 반환
    
    if node.key < root.key: # 추가하려는 node의 키가 root키 보다 작으면
        root.left = insert_bst(root.left, node) # 왼쪽 서브트리로 넣어야 함
    else: # 추가하려는 node의 키가 root키 보다 크면
        root.right = insert_bst(root.right, node) # 오른쪽 서브트리로 넣어야 함
    
    return root # root를 반환 ( root 변환 없음 )

def delete_bst(root, key): # 이진탐색트리의 삭제 연산
    if root == None: # root노드가 공백이면
        return root # 공백 트리
    
    if key < root.key: # 삭제하려는 키가 root의 키값보다 작으면
        root.left = delete_bst(root.left, key) # 왼쪽 서브트리로 진행
    elif key > root.key: # 삭제하려는 키가 root의 키값보다 크면
        root.right = delete_bst(root.right, key) # 오른쪽 서브트리로 진행

    # 삭제하려는 key가 루트의 키와 같으면 root를 삭제
    else:
        if root.left == None: # case1(단말노드) 또는 case2(오른쪽 자식만 있는 경우)
            return root.right
        
        if root.right == None: # case2(왼쪽 자식만 있는 경우)
            return root.left
        
        succ = search_min_bst(root.right) # case3 (두 자식이 모두 있는 경우)
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)
    
    return root