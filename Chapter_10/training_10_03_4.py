# 코드 10.3
from queue import Queue
def BFS_AL(vtx, aList, s): # 너비우선탐색 ( 인접 리스트 방식 )
    n = len(vtx) # 그래프 정점의 수
    visited = [False]*n # 방문확인 리스트
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty(): # 탐색이 끝날 때까지 반복
        s = Q.get() # 큐에서 정점 꺼냄
        print(vtx[s], end=' ') # 정점 출력
        for v in aList[s]: # s의 이웃 정점 v가
            if visited[v] == False: # 아직 방문 하지 않았다면
                Q.put(v) # 큐에 삽입하고
                visited[v] = True # 방문 했다 표시
                
# 코드 10.4

vtx = ['A','B','C','D','E','F','G','H'] # 그래프의 정점들
aList = [[1,2], # A와 연결된 인덱스 : B C
         [0,3], # B와 연결된 인덱스 : A D
         [0,3,4], # C와 연결된 인덱스 : A D E
         [1,2,5], # D와 연결된 인덱스 : B C F
         [2,6,7], # E와 연결된 인덱스 : C G H
         [3], # F와 연결된 인덱스 : D
         [4,7], # G와 연결된 인덱스 : E H
         [4,6]] # H와 연결된 인덱스 : E G

vtx = ['A','B','C','D','E','F','G','H'] # 그래프의 정점들
aList1 = [[1,2], # A와 연결된 인덱스 : B C
         [0,3,5], # B와 연결된 인덱스 : A D
         [0,5], # C와 연결된 인덱스 : A D E
         [1,4,7], # D와 연결된 인덱스 : B C F
         [3,7], # E와 연결된 인덱스 : C G H
         [1,2,6], # F와 연결된 인덱스 : D
         [5], # G와 연결된 인덱스 : E H
         [3,4]] # H와 연결된 인덱스 : E G
print('BFS_AL(출발 : A) : ',end = '')
BFS_AL(vtx, aList1, 0)
print()