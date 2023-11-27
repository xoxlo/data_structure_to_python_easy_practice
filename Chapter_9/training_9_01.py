class BSTNode: # 이진탐색트리를 위한 노드 클래스
    def __init__(self, key, value): # 생성자 ( 키와 값을 받음 )
        self.key = key
        self.value = value
        self.left = None
        self.right = None