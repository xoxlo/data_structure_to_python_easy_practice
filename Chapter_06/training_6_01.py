class Node: # 단순 연결 노드
    def __init__(self, elem, link=None):
        self.data = elem # 해당 노드의 데이터
        self.link = link # 해당 노드가 다음 노드를 가리키는 링크