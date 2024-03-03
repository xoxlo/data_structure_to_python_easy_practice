from training_5_01_03 import CircularQueue

# 스택의 연산 : 클래스의 멤버 함수로 구현
class ArrayStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = [None]*capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity-1

    def push(self, e): # 스택 - 삽입
        if not self.isFull(): # 포화상태가 아니라면
            self.top+=1 # top 위치를 +1 하고
            self.array[self.top] = e # 새로운 top 위치에 새로운 항목 e를 삽입
        else:
            pass
        
    def pop(self): # 스택 - 삭제
        if not self.isEmpty(): # 빈상태가 아니라면
            self.top -= 1 # top 위치 -1 하고
            return self.array[self.top+1] # 삭제하려고 하던 top+1 위치를 가져옴.
        else:
            pass
            
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass # 언더플로 예외, d처리하지 않음.
        
    def __str__(self):
        return str(self.array[0:self.top+1])

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

def isValidPos(x, y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def DFS():
    print('DFS : ')
    stack = ArrayStack(100)
    stack.push((0,1)) # 시작위치 설정
    
    while not stack.isEmpty():
        here = stack.pop()
        print(here, end='->')
        (x,y) = here # 현재 위치의 x, y 좌표 추출
        
        
        if (map[y][x] == 'x'): # (x, y)가 출구 위치이면
            return True # 탈출 성공
        
        else:
            map[y][x] = '.' # 현재 위치 방문 ' . ' 표시
            if isValidPos(x, y - 1): stack.push((x, y - 1)) # 상
            if isValidPos(x, y + 1): stack.push((x, y + 1)) # 하
            if isValidPos(x - 1, y): stack.push((x - 1, y)) # 좌
            if isValidPos(x + 1, y): stack.push((x + 1, y)) # 우
        print(" 현재 스택 : ", stack)
    return False                    

def BFS():
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS : ')
    while not que.isEmpty():
        here = que.dequeue()
        print(here,end='->')
        x,y = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1): # 상
                que.enqueue((x, y-1))
            if isValidPos(x, y+1): # 하
                que.enqueue((x, y+1))
            if isValidPos(x-1, y): # 좌
                que.enqueue((x-1, y))
            if isValidPos(x+1, y): # 우
                que.enqueue((x+1, y))
    return False