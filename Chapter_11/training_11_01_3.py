# 코드 실습 11.1

vertex = ['A',      'B',    'C',    'D',    'E',    'F',    'G']
weight = [[None,    29,     None,   None,   None,   10,     None],
          [29,      None,   16,     None,   None,   None,   15  ],
          [None,    16,     None,   12,     None,   None,   None],
          [None,    None,   12,     None,   22,     None,   18  ],
          [None,    None,   None,   22,     None,   27,     25  ],
          [10,      None,   None,   None,   27,     None,   None],
          [None,    15,     None,   18,     25,     None,   None]]



# 코드 실습 11.2

def weightSum(vlist, W): # 정점리스트, 인접 행렬(가중치값이 존재)을 매개변수로
    sum = 0 # 가중치 합산 초기값 설정
    for i in range(len(vlist)): # 모든 정점에 대해 반복
        for j in range(i+1, len(vlist)): # 하나의 행에 대해 ( 한쪽 삼각면만 )
            if W[i][j] != None: # 간선이 있으면
                sum += W[i][j] # 가중치의 값을 합함
    return sum # 최종 가중치의 합 반환

print('AM : weight Sum => ',weightSum(vertex, weight))



# 코드 실습 11.3

def printAllEdges(vlist, W): # 정점리스트, 인접 행렬을 매개변수로
    for i in range(len(vlist)): # 모든 정점에 대해 반복
        for j in range(i+1, len(vlist)): # 하나의 행에 대해 ( 한쪽 삼각면만 )
            if W[i][j] != None and W[i][j] != 0: # None, 0이 아니면, 즉 연결 되어있는 간선이어야함
                print("(%s, %s, %d)" %(vlist[i],vlist[j],W[i][j]), end=' ') # 연결 되어있는 간선 출력
    print()

printAllEdges(vertex,weight)