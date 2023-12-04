from CircularQueue import *

class TNode: # 이진트리를 위한 노드 클래스
    def __init__(self, data, left, right):
        self.data = data # 데이터
        self.left = left # 왼쪽 자식 링크
        self.right = right # 오른쪽 자식 링크
        
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

def levelorder(root): # 이진트리 - 레벨순회
    queue = CircularQueue() # 큐 객체 초기화
    queue.enqueue(root) # 최초 큐에는 루트 노드만 있음
    while not queue.isEmpty(): # 큐가 공백 상태가 아닌 동안
        n = queue.dequeue() # 큐에서 맨 앞의 n을 꺼냄
        if n is not None:
            print(n.data, end='') # 노드의 정보 출력
            queue.enqueue(n.left) # 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right) # 오른쪽 자식 노드를 큐에 삽입