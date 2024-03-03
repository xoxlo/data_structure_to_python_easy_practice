import math
from training_5_10 import *
from training_5_05_6 import *

(ox,oy) = (8,2)
def dist(x,y):
    (dx,dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx+dy*dy)

def isValidPos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,1,-dist(0,1)))
    print('PQueue : ')
    
    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end='->')
        x,y,_ = here;
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x,y-1):
                q.enqueue((x,y-1,-dist(x,y-1)))
            if isValidPos(x,y+1):
                q.enqueue((x,y+1,-dist(x,y+1)))
            if isValidPos(x-1,y):
                q.enqueue((x-1,y,-dist(x-1,y)))
            if isValidPos(x+1,y+1):
                q.enqueue((x+1,y,-dist(x+1,y)))
        print('우선순위큐 : ',q)
    return False

map=[['1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1', '1', '0', 'x'],
    ['1', '0', '0', '0', '1', '0', '0', '0', '1'],
    ['1', '1', '1', '0', '1', '1', '1', '0', '1'],
    ['1', '0', '0', '0', '1', '0', '0', '0', '1'],
    ['1', '0', '1', '1', '1', '0', '1', '1', '1'],
    ['1', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1']]

MAZE_SIZE = 9
result = MySmartSearch()
if result : print('--> 미로탐색 성공')
else: print('--> 미로탐색 실패')