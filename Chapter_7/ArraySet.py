class ArraySet:
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def __str__(self):
        return str(self.array[0:self.size])
        
    def contains(self, e): # 선택한 집합에 원소 e가 포함되어있는지 판단
        for i in range(self.size):
            if self.array[i] == e:
                return True # 원소 e가 있으면 True 반환
        return False # 원소 e가 없으면 False 반환

    def insert(self, e): # 선택한 집합에 원소 e를 삽입
        if not self.contains(e) and not self.isFull(): # 집한 안에 똑같은 원소 e가 없어야 하고 포화상태가 아니어야함.
            self.array[self.size] = e # 원소 e 삽입
            self.size += 1 # 원소 e를 삽입했으니 배열 size +1
            
    def delete(self, e): # 선택한 집합에 원소 e를 삭제
        for i in range(self.size): # 배열 전체 범위를 반복
            if self.array[i] == e: # 원소 e와 같은 값이 i 위치에 있다면
                self.array[i] = self.array[self.size-1] # 맨 뒤 원소를 삭제할 위치에 복사하고 원소 e를 삭제
                self.size -= 1 # 원소 e 하나를 삭제 했으니 size -1
                return
    # 합집합
    def union(self,setB): # 처음 self가 setA라고 생각하면 된다.
        setC = ArraySet() # 집합A와 집합B의 union한 원소들을 저장할 공간
        for i in range(self.size):
            setC.insert(self.array[i]) # 집합A의 원소들을 임의의 집합C에 전체 삽입
        for i in range(setB.size): # 집합B 원소들 만큼 반복
            if not setC.contains(setB.array[i]): # 집합B 각 원소들이 집합C 안의 원소가 포함 되어있지 않을때
                setC.insert(setB.array[i]) # 집합C에 원소를 추가
        return setC # 집합C 반환 - 합집합
    
    # 교집합
    def intersect(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]): # 집합A의 각 원소들이 집합B에 포함이 되어있다면
                setC.insert(self.array[i]) # 임의의 집합C에다가 원소 삽입
        return setC # 집합C 반환 - 교집합
    
    # 차집합
    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]): # 집합A의 각 원소들이 집합B에 포함이 안되어있다면
                setC.insert(self.array[i]) # 임의의 집합C에다가 원소 삽입
        return setC # 집합C 반환 - 차집합
    
    
    # 두 집합이 같은 집합인지 검사
    def equals(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]): # 집합A와 집합B의 차집합한 결과
                setC.insert(self.array[i]) # 집합C에다가 저장
                
        if setC.isEmpty(): # 만약 집합C에 공백일 시
            return True # 두 집합은 같은 집합
        else:
            return False # 다를 시 두 집합은 다른 집합
        
    def __eq__(self, setB):
        if self.array == setB.array:
            return True
        else:
            return False