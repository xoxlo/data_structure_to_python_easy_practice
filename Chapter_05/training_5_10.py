from training_5_01_03 import *

class PriorityQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0 # 요소의 수를 나타냄
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, e):
        if not self.isFull():
            self.array[self.size] = e
            self.size += 1
    
    def findMaxIndex(self):
        if self.isEmpty():
            return -1
        highest = 0
        for i in range(1, self.size):
            if self.array[i][2] > self.array[highest][2]:
                highest = i
        return highest
    
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest != -1:
            self.size -= 1
            self.array[highest], self.array[self.size] = \
                self.array[self.size], self.array[highest]
            return self.array[self.size]
    
    def peek(self):
        highest = self.findMaxIndex()
        if highest != -1:
            return self.array[highest]
        
    def __str__(self):
        return str(self.array[0:self.size])