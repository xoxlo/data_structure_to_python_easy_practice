class CircularQueue:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.array = [None]*capacity
        self.front = 0
        self.rear = 0
        
    def isEmpty(self):
        return self.front == self.rear # 공백 상태 -> (front == rear)
    
    def isFull(self):
        return self.front == (self.rear+1)%self.capacity # 포화 상태 -> rear 다음 front면 포화 상태
    
    def enqueue(self, item):
        if not self.isFull(): # 포화 상태가 아니라면
            self.rear = (self.rear+1)%self.capacity # rear위치를 +1 하고
            self.array[self.rear] = item # rear위치에다가 요소 삽입
        else:
            pass # Overflow 예외, 처리 안함
    
    def dequeue(self):
        if not self.isEmpty(): # 공백 상태가 아니라면
            self.front = (self.front+1)%self.capacity # front위치를 +1 하고
            return self.array[self.front] # front위치에 있는 요소 삭제
        else:
            pass # Underflow 예외, 처리 안함
        
    def peek(self):
        if not self.isEmpty(): # 공백 상태가 아니라면
            return self.array[self.front+1]%self.capacity # front위치는 변경 X, front+1 위치의 요소를 반환
        else:
            pass # Underflow 예외, 처리 안함
        
    def size(self):
        return (self.rear - self.front + self.capacity)%self.capacity # 큐의 전체 요소의 수 계산
    
    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else:
            return str(self.array[self.front+1:self.capacity] + \
                        self.array[0:self.rear+1])
            
            
            
def levelorder(root): # 이진트리 - 레벨순회
    queue = CircularQueue(100) # 큐 객체 초기화
    queue.enqueue(root) # 최초 큐에는 루트 노드만 있음
    while not queue.isEmpty(): # 큐가 공백 상태가 아닌 동안
        n = queue.dequeue() # 큐에서 맨 앞의 n을 꺼냄
        if n is not None:
            print(n.data, end='') # 노드의 정보 출력
            queue.enqueue(n.left) # 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right) # 오른쪽 자식 노드를 큐에 삽입
