def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                print("(",vtx[s], vtx[v], ")", end=' ')
                ST_DFS(vtx, adj, v, visited)
                
                
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
ST_DFS(vtx,edge,0,[False]*len(vtx))