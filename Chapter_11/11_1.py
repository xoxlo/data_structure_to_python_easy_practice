# 연습문제 11_1

# 인접 행렬 표현
vertex = ['A','B','C','D','E','F',]
weight = [[None, 50  , None,   20, None, None],
          [50  , None,   10, None,   20, None],
          [None, 10  , None, None,   35, None],
          [20  , None, None, None,   15, None],
          [None, 20  ,   35,   15, None,    3],
          [None, None, None, None,    3, None]]

# 인점 리스트 표현 -> 딕셔너리와 집합 이용
graph = {'A' : {('B', 50),('D', 20)},
          'B' : {('A', 50), ('C', 10), ('D',15)},
          'C' : {('B', 10), ('E', 35)},
          'D' : {('A', 20), ('B', 15), ('E', 15)},
          'E' : {('B', 20), ('C', 35), ('D', 15), ('F', 3)},
          'F' : {('E', 3)}}