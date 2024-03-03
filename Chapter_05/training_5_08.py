from training_5_01_03 import *

class CircularDeque(CircularQueue): # 부모 클래쓰 CirculaQueue로 하고 자식 클래쓰는 CircularDeque이다. 즉 Deque은 Queue안에 있는 멤버함수(메소드) 등 사용 가능
    def __init__(self, capacity=10):
        super().__init__(capacity)

# isEmpty(), isFull(), size(), __str__()는 부모 클래쓰에 있음.

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

## 새로 구현이 필요한 연산들
    def addFront(self,item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front-1+self.capacity)%self.capacity
        else:
            pass
        
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear-1+self.capacity)%self.capacity
            return item
        else:
            pass
        
    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            pass