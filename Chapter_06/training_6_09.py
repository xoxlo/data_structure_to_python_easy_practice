class DNode: # 이중 연결 리스트를 위한 노드
    def __init__ (self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next