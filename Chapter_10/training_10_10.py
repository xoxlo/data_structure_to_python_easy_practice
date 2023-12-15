def ST_DFS(vtx, adj, s, visited): # 신장트리 DFS 방법
    visited[s] = True # 현재 s 정점 방문 표시
    for v in range(len(vtx)): # 정점의 수 만큼 반복
        if adj[s][v] != 0: # 정점 s, v가 연결이 되어있다면
            if visited[v] == False: # 그리고 정점 v를 방문하지 않았다면
                print("(",vtx[s], vtx[v], ")", end=' ') # s v 출력
                ST_DFS(vtx, adj, v, visited) # 순환 반복 -> 정점 v를 시작점으로
                
                
vtx = ['A','B','C','D','E','F','G','H']
edge = [[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]

print("신장트리(DFS) : ", end='')
ST_DFS(vtx,edge1,0,[False]*len(vtx))