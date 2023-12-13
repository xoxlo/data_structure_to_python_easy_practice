# 코드 실습 11.16

INF = 9999 # INF는 정점간 간선 연결이 안되있다는 뜻 ( 무제한으로 표시 )
def printA(A): # A 행렬을 화면에 출력. 정점간 간선의 가중치를 알 수 있음
    vsize = len(A)
    print("===================================")
    for i in range(vsize):
        for j in range(vsize):
            if (A[i][j] == INF):
                print(" INF ", end='')
            else:
                print("%4d " %A[i][j], end='')
        print("");
        
def shortest_path_floyd(vertex, adj): # Floyd의 최단경로탐색 함수
    vsize = len(vertex) # 정점의 개수
    A = list(adj) # 인접행렬을 리스트로 가져옴
    for i in range(vsize): # 정점의 개수 만큼 반복
        A[i] = list(adj[i]) # 인접행렬 adj를 A에다가 똑같이 복사 ( 2차원 배열 )
    for k in range(vsize): # 0번 정점부터 n-1까지 순서대로 적용
        for i in range(vsize):
            for j in range(vsize):
                if (A[i][k] + A[k][j] < A[i][j]): # i정점에서 j정점까지 가는 거리 보다 i->k, k->j까지 거쳐서 가는게 더 빠르면
                    A[i][j] = A[i][k] + A[k][j] # 그 경로를 i->j 경로로 갱신
        printA(A) # 현재 A 행렬 출력
                    
vertex = ['A',     'B',   'C',   'D',   'E',   'F',   'G']
weight = [[0  ,      7,   INF,   INF,   INF,    10,   INF],
          [7  ,      0,   4  ,   INF,   INF,   INF,   INF],
          [INF,      4,   0  ,     2,   INF,   INF,   INF],
          [INF,    INF,   2  ,     0,    11,   INF,   4  ],
          [3  ,      2,   INF,    11,     0,    27,   5  ],
          [10 ,      6,   INF,     9,    27,     0,   INF],
          [INF,    INF,   INF,     4,     5,   INF,   0  ]]

print("Shortest Path By Floyd's Algorithm")
shortest_path_floyd(vertex, weight)