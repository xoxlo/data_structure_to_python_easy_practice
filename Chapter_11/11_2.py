# 연습문제 11_2

# 인접 행렬 표현
vertex = ['A','B','C','D','E','F',]
weight = [[None, 50  ,   45,   20, None, None],
          [None, None,   10,   15,   20, None],
          [None, None, None, None,   30, None],
          [10  , None, None, None,   15, None],
          [None, 20  ,   35, None, None, None],
          [None, None, None, None,    3, None]]

# 인접 리스트 표현
graph = {'A' : {('B', 50), ('C', 45), ('D', 20)},
          'B' : {('C', 10), ('D', 15), ('E', 20)},
          'C' : {('E', 35)},
          'D' : {('A', 10), ('E', 15)},
          'E' : {('B', 20), ('C', 35)},
          'F' : {('E', 3)}}