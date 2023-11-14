from training_6_01 import Node

class LinkedStack :
    def __init__(self):
        self.top = None
        self.count = 0
        
    def isEmpty(self): # 공백 상태 검사
        return self.top == None
    
    def isFull(self): # 포화 상태 검사
        return False
    
    def push(self, count): # 삽입 연산
        count += 1 # 삽입시 count +1
        self.top = Node(e, self.top) # 요소 e를 이용해 노드를 만들고 링크를 상단 노드로 연결 ( 이제 이 노드가 상단임 )
    
    # def push(self, e):
    # n = Node(e)
    # n.link = self.top
    # self.top = n
    
    def pop(self): # 삭제 연산
        if not self.isEmpty(): # 공백상태인지 검사
            self.count -= 1 # 삭제시 count -1
            n = self.top # n이 현재 상단 가리킴
            self.top = n.link # 상단 다음 노드의 링크가 top을 가리킴 
            return n.data # n의 data 반환
        
    def peek(self):
        if not self.isEmpty():
            return self.top.data # 현재 상단에 있는 노드의 데이터 반환
        
    def size(self): # 전체 요소의 수 계산
        node = self.top
        count = 0
        while not node == None: # None이 아니면
            node = node.link # 다음 노드 이동
            count += 1 # count +1
        return count # 최종 count 반환
    
    def size(self):
        return count

    def __str__(self): # 문자열 변환 함수
        arr = []
        node = self.top
        while not node == None:
            arr.append(node.data)
            node = node.link
        return str(arr)