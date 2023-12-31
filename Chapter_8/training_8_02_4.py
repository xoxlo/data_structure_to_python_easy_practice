def preorder(n): # 전위순회 함수 ( VLR )
    if n is not None:
        print(n.data, end = ' ') # 루트노드
        preorder(n.left) # LEFT 처리
        preorder(n.right) # RIGHT 처리
        
def inorder(n): # 중위순회 함수 ( LVR )
    if n is not None:
        inorder(n.left) # LEFT 처리
        print(n.data, end = ' ') # 루트노드
        inorder(n.right) # RIGHT 처리
        
def postorder(n): # 후위순회 함수 ( LRV )
    if n is not None:
        postorder(n.left) # LEFT 처리
        postorder(n.right) # RIGHT 처리
        print(n.data, end = ' ') # 루트노드