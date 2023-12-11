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

def weightSum(vlist, W): # 정점리스트 , 인접 행렬을 매개변수로
    sum = 0 # 가중치 합산 초기값 설정
    for i in range(len(vlist)): # 모든 정점에 대해
        for j in range(i+1, len(vlist)): # 하나의 행에 대해 ( 한쪽 삼각 면만 )
            if W[i][j] != None: # 간선이 있으면
                sum += W[i][j] # 가중치의 값을 합함
    return sum # 최종 가중치의 합 반환

print('AM : weight Sum => ',weightSum(vertex, weight))