# 코드 10.1

def DFS(vtx, adj, s, visited): # 깊이우선탐색 ( 인접 행렬 방식 )
    print(vtx[s], end=' ') # 현재 정점 s 방문 -> 출력
    visited[s] = True # 방문한 곳은 True
    
    for v in range(len(vtx)): # 그래프의 모든 정점 반복
        if adj[s][v] != 0: # 만약 false가 아니라면 반복 ( false면 정점간 연결이 안되있는거임 )
            if visited[v] == False: # 방문하지 않은 v가 있다면
                DFS(vtx, adj, v, visited) # v를 시작으로 다시 순환 호출

# 코드 10.2

vtx = ['A','B','C','D','E','F','G','H']
edge = [[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]
print('DFS(출발 : A) : ',end='')
DFS(vtx,edge,0,[False]*len(vtx)) # visite를 False로 전달 why? 초기 상태는 방문 X
print()