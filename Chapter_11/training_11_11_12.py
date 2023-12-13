# 코드 실습 11.11

INF = 9999 # 가장 큰 가중치 (무한대)

def getMinVertex(dist, selected): # 인접한 정점들의 간선의 가중치가 제일 작은 것을 탐색하는 함수
    minv = 0
    mindist = INF
    for v in range(len(dist)): # dist에는 간선 간의 가중치가 제일 작은 값을 저장
        if not selected[v] and dist[v]<mindist : # MST에 포함 되어있지 않고(선택되지 않았고), mindist보다 dist[v]가 더 작으면
            mindist = dist[v] # mindist는 제일 작은 가중치인 dist[v]로 재갱신
            minv = v # dist리스트 중에서 v번째가 그 다음으로 작음
    return minv # 최소 정점 변환

# 코드 실습 11.12

def MSTPrim(vertex, adj):
    vsize = len(vertex) # 정점의 개수
    dist = [INF] * vsize # 가장 가까운 거리를 저장할 리스트
    selected = [False] * vsize # 선택이 됐는지 확인하기 위한 리스트
    dist[0] = 0 # 시작 점은 거리가 0
    
    for i in range(vsize): # 정점의 수 만큼 반복
        u = getMinVertex(dist, selected) # 인접한 정점들의 간선의 가중치가 제일 작은 것을 u로 반환
        selected[u] = True # u번째 인덱스는 True, 선택이 되었다는 뜻
        print(vertex[u], end=' ') # u번째 점정 출력
        
        for v in range(vsize): # 정점의 수 만큼 반복
            if (adj[u][v] != None): # u, v 서로 연결이 되어있다면 ( None은 연결이 안되있음을 말함 )
                if selected[v] == False and adj[u][v] < dist[v]: # 정점 u, v의 가중치가 dist[v]보다 작으면
                    dist[v] = adj[u][v] # dist에 가중치 재경신, why? 기존에 있던 가중치보다 더 작기 때문
    print()
    
vertex = ['A',      'B',    'C',    'D',    'E',    'F',    'G']
weight = [[None,    29,     None,   None,   None,   10,     None],
          [29,      None,   16,     None,   None,   None,   15  ],
          [None,    16,     None,   12,     None,   None,   None],
          [None,    None,   12,     None,   22,     None,   18  ],
          [None,    None,   None,   22,     None,   27,     25  ],
          [10,      None,   None,   None,   27,     None,   None],
          [None,    15,     None,   18,     25,     None,   None]]

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)