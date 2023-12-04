class TNode: # 이진트리를 위한 노드 클래스
    def __init__(self, data, left, right):
        self.data = data # 데이터
        self.left = left # 왼쪽 자식 링크
        self.right = right # 오른쪽 자식 링크