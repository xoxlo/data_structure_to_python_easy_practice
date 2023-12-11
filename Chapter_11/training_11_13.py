INF = 9999

def choose_vertex(dist, found):
    min = INF
    minpos = -1
    for i in range(len(dist)):
        if dist[i] < min and found[i] == False:
            min = dist[i]
            minpos = i
    return minpos;


def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True
    dist[start] = 0
    
    for i in range(vsize):
        print("Step %2d : "%(i+1), dist)
        u = choose_vertex(dist, found)
        found[u] = True
        
        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u
                    
    return path