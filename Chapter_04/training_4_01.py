capacity = 10
array = [None]*capacity
top = -1

# 스택의 연산 : 일반 함수

def isEmpty():
    if top == -1 :
        return True
    else :
        return False
    
def isFull():
    return top == capacity-1

def push(e): # 스택 - 삽입
    global top # top은 전역변수
    if not isFull(): # 포화상태가 아니라면
        top+=1 # top 위치를 +1 하고
        array[top] = e # 새로운 top 위치에 새로운 항목 e를 삽입
    else:
        print("Stack Overflow !")
        exit()
        
def pop(): # 스택 - 삭제
    global top # top은 전역변수
    if not isEmpty(): # 빈상태가 아니라면
        top -= 1 # top 위치 -1 하고
        return array[top+1] # 삭제하려고 하던 top+1 위치를 가져옴.
    else:
        print("Stack Underflow !")
        exit()

def peek():
    if not isEmpty():
        return array[top]
    else:
        pass # 언더플로 예외, 처리하지 않음.