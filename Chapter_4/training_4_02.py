
# 스택의 연산 : 클래스의 멤버 함수로 구현

class ArrayStack:
    def __init__(self,capacity):
        self.capacity = 10
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
