from training_4_02 import ArrayStack

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

result = DFS()
if result : print(" ---> 미로탈출 성공 !")
else: print(" ---> 미로탈출 실패 !")