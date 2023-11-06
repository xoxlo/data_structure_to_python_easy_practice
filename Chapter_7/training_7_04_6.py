class SortedArraySet:
    def __init__( self, capacity=100 ):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty( self ):
       return self.size == 0

    def isFull( self ):
       return self.size == self.capacity

    def __str__( self ) :
        return str(self.array[0:self.size])

    # 이진탐색 사용 가능 ***
    def contains(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                return True
        return False

    def append(self, e) :
        self.array[self.size] = e
        self.size += 1

        
def insert(self, e): # 정렬된 배열을 이용한 집합의 insert 연산 재정의
    if self.contains(e) or self.isFull(): # e가 포함되거나 포화상태면
        return # 그냥 리턴, 삽입 못함
    
    self.array[self.size] = e # 일단 정렬된 배열의 맨 뒤에 추가
    self.size += 1 # size +1
    

    for i in range(self.size-1, 0, -1): # 맨 뒤에서부터 맨 앞까지 반복
        if self.array[i-1] <= self.array[i]: # 이 과정을 작거나 같은 원소가 나올 때까지 반복
            break
        self.array[i-1], self.array[i] = self.array[i], self.array[i-1] # 원소 교환
        
        
def __eq__(self, setB):
    if self.size != setB.size: # 원소의 개수가 다르면
        return False # False , why? 개수가 같은 집합이 어차피 안되니까
    
    # 만약 집합의 원소들이 정렬되어 있다면?
    # if self.array[i] != setB.array[i]:로 25행을 변경해도 된다.
    # 이렇게 할 시 시간복잡도는 O(n^2)에서 O(n)으로 줄어든다.
    # 정렬을 이용한 엄청난 개선
    
    for i in range(self.size): # 원소의 개수만큼 반복
        if not setB.contains(self.array[i]): # 원소 하나하나가 setB에 포함되어있는지 확인
            return False # 포함되어 있지 않으면 False
    return True

def union(self, setB):
    setC = SortedArraySet()
    i = 0 # 집합 self 원소 인덱스
    j = 0 # 집합 setB 원소 인덱스
    while i < self.size and j < setB.size :
        a = self.array[i]
        b = self.array[j]
        if a == b: # 두 집합의 원소가 같으면
            setC.append(a) # setC(합집합)의 맨 뒤에 추가, 그리고 두 집합 인덱스 +1
            i += 1 
            j += 1
        elif a < b:
            setC.append(a) # self의 원소가 setB의 원소보다 작으면 setC(합집합)의 맨 뒤에 추가, self 집합 인덱스 +1
            i += 1
        else :
            setC.append(b) # 그렇지 않으면 setB의 원소를 setC(합집합)의 맨 뒤에 추가, setB 집합 인덱스 +1
            j += 1 
    
    while i < self.size : # self의 원소가 남아 있으면
        setC.append(self.array[i]) # setC(합집합)에 추가
        i += 1
    while j < setB.size : # setB의 원소가 남아 있으면
        setC.append(setB.array[j]) # setC(합집합)에 추가
        j += 1
        
    return setC # 최종 setC(합집합)을 반환