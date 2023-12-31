class ArrayList:
    # 리스트의 데이터 -> 생성자에서 정의 및 초기화
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0
        
    # 리스트의 연산 -> 클래스의 메소드
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else: return None
    
    def insert(self, pos, e):
        if not self.isFull() and 0<=pos<=self.size:
            for i in range(self.size,pos,-1): # pos 이후의 모든 항목을 뒤로 한 칸씩 이동
                self.array[i] = self.array[i-1]
            self.array[pos] = e # pos 위치에 e(새로운 항목)를 삽입
            self.size += 1 # 항목을 추가시켰으니 size +1
        else: pass
    
    def delete(self, pos):
        if not self.isEmpty() and 0<=pos<=self.size:
            e = self.array[pos] # 삭제할 항목을 복사
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1] # pos 이후의 항목들을 앞으로 한 칸씩 이동
            self.size -= 1 # 항목을 삭제했으니 size -1
            return e # 복사해둔 항목 반환
        else: pass
        
    def replace(self, pos, e):
        if not self.isEmpty() and 0<=pos<=self.size:
            self.array[pos] = e # pos 위치에 새로운 e 항목을 대체 
        else: pass
        
    def count(self, e):
        cnt = 0
        for i in range(0, self.size):
            if self.array[i] == e:
                cnt+=1
        return cnt
                
    def __str__(self):
        return str(self.array[0:self.size])  # string으로 Array 출력
    
    def findMax_me(self):
        max = self.array[0]
        for i in range(0, self.size-1):
            if max < self.array[i]:
                max = self.array[i]
            elif self.isEmpty():
                return -1
        return max
    
    def findMax_answer(self):
        if self.isEmpty():
            return -1
        max = 0
        for i in range(1, self.size):
            if self.array[max] < self.array[i]:
                max = i
        return max