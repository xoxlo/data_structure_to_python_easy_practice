from training_8_01 import TNode
from training_8_10_11 import *
def make_morse_tree(): # 모스 부호 코드 결정트리 만드는 함수
    root = TNode(None, None, None) # 루트를 트리노드를 이용
    for tp in table: # 모스 부호가 정의 되어있는 테이블을 가져와서 반복
        code = tp[1] # 1번째 인덱스가 모스부호기호를 가지고 있음
        node = root
        for c in code: # 모스부호가 가진 각 부호를 c에 넣어주면서 반복
            if c == '.': # c가 .이면 (왼쪽으로 진행)
                if node.left == None: # 왼쪽 노드가 비어있다면
                    node.left = TNode(None, None, None) # 노드 생성
                node = node.left # 노드가 있으면 그 노드로 이동
            elif c == '-': # c가 -이면 (오른쪽으로 진행)
                if node.right == None: # 오른쪽 노드가 비어있다면
                    node.right = TNode(None, None, None) # 노드 생성
                node = node.right # 노드가 있으면 그 노드로 이동
                
        node.data = tp[0] # 0번째 인덱스인 알파뱃을 노드의 데이터에 저장
    return root

def decode(root, code): # 디코딩 함수
    node = root
    for c in code: # 모스부호부호를 빼주면서 반복
        if c == '.': # .이면
            node = node.left # 왼쪽으로 이동
        elif c == '-': # -이면
            node = node.right # 오른쪽으로 이동
    return node.data # 그 모스부호에 맞는 데이터(알파뱃)를 가져옴
