from training_5_01_03 import *
from training_5_08 import *
        
Q = CircularQueue(10)
D = CircularDeque(10)
for i in range(1, 9):
    D.addRear(i)
print(D)
for i in range(1, 9):
    Q.enqueue(D.deleteRear())
for i in range(1, 9):
    D.addRear(Q.dequeue())
print(D)