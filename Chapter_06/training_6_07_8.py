from training_6_01 import Node
class LinkedQueue:
    def __init__(self):
        self.tail = None
        
    def isEmpty(self):
        return self.tail == None # tail이 None이면 공백
    def isFull(self):
        return False # 연결된 구조에서 포화 상태는 의미 없음
    
    def enqueue(self, item): # 삽입
        node = Node(item, None)
        if self.isEmpty(): # 공백 상태에서 삽입
            self.tail = node
            node.link = node
        else: # 공백 아닌 상태에서 삽입
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
            
    def dequeue(self): # 전단 요소 삭제
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
        
    
    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count
        
    def __str__(self):
        arr = []
        if not self.isEmpty():
            node = self.tail.link # node는 front노드
            while not node == self.tail: # 노드와 front노드와 같을 때 반복문 종료
                arr.append(node.data) # 노드의 데이터를 arr에 추가
                node = node.link # 다음 노드 진행
            arr.append(node.data) # 마지막으로 rear의 데이터 추가
        return str(arr) # 리스트 반환