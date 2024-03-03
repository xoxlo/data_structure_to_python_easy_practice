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
    
def count_node(n): # 순환을 이용해 트리의 노드 수 계산하는 함수
    if n is None: # n이 None이면 공백트리, 0을 반환
        return 0
    else: # 좌우 서브트리의 노드 수의 합 + 1을 반환
        return 1 + count_node(n.left) + count_node(n.right)
    
def count_leaf(n): # 단말 노드 수 계산 함수
    if n is None: # 공백트리 -> 0 반환
        return 0
    elif n.left is None and n.right is None: # 단말노드 -> 1 반환
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right) # 비단말 노드 -> 좌 + 우 결과 합

def calc_height(n): # 이진트리의 높이 계산 함수
    if n is None: # 공백 트리 -> 0 반환
        return 0
    hLeft = calc_height(n.left) # 왼쪽트리의 높이
    hRight = calc_height(n.right) # 오른쪽트리의 높이
    if (hLeft > hRight): # 높이는 좌,우 어느 곳이든 상관없으니까 더 높은 트리에다가 +1을 해주면서 반환
        return hLeft + 1
    else:
        return hRight + 1

g = TNode('G',None,None)
h = TNode('H',None,None)
d = TNode('D',None,None)
b = TNode('B',d,None)
e = TNode('E',g,h)
f = TNode('F',None,None)
c = TNode('C',e,f)
root = TNode('A',b,c)

print("\n========== CHAPTER 9 연습문제 8.18 왼쪽 트리==========")    
print('\nIn-Order    : ', end='') # 중위 순회 ( LVR )
inorder(root)
print('\nPre-Order   : ', end='') # 전위 순회 ( VLR )
preorder(root)
print('\nPost-Order  : ', end='') # 후위 순회 ( LRV )
postorder(root)
print('\nLevel-Order : ', end='') # 레벨 순회
levelorder(root)
print()
print("노드의 개수 = %d개" % count_node(root))
print("단말의 개수 = %d개" % count_leaf(root))
print("트리의 높이 = %d" % calc_height(root))


a = TNode('A',None,None)
b = TNode('B',None,None)
c = TNode('C',None,None)
e = TNode('E',None,None)
d = TNode('D',None,None)
slash = TNode('/',a,b)
aster = TNode('*',TNode('*',slash,c),d)
root = TNode('+',aster,e)

print("\n========== CHAPTER 9 연습문제 8.18 오른쪽 트리==========")    
print('\nIn-Order    : ', end='') # 중위 순회 ( LVR )
inorder(root)
print('\nPre-Order   : ', end='') # 전위 순회 ( VLR )
preorder(root)
print('\nPost-Order  : ', end='') # 후위 순회 ( LRV )
postorder(root)
print('\nLevel-Order : ', end='') # 레벨 순회
levelorder(root)
print()
print("노드의 개수 = %d개" % count_node(root))
print("단말의 개수 = %d개" % count_leaf(root))
print("트리의 높이 = %d" % calc_height(root))