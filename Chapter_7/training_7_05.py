# 3장에서 다룬 ArraySet 클래스 불러오기~
from ArraySet import *

def insert(self, e): # 정렬된 배열을 이용한 집합의 insert 연산 재정의
    if self.contains(e) or self.isFull(): # e가 포함되거나 포화상태면
        return # 그냥 리턴, 삽입 못함
    
    self.array[self.size] = e # 일단 정렬된 배열의 맨 뒤에 추가
    self.size += 1 # size +1
    

    for i in range(self.size-1, 0, -1): # 맨 뒤에서부터 맨 앞까지 반복
        if self.array[i-1] <= self.array[i]: # 이 과정을 작거나 같은 원소가 나올 때까지 반복
            break
        self.array[i-1], self.array[i] = self.array[i], self.array[i-1] # 원소 교환