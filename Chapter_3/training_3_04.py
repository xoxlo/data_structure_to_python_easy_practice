from training_3_03 import ArrayList
L = ArrayList(50)

print("최초 ",L)
L.insert(0,100)
L.insert(0,200)
L.insert(1,300)
L.insert(L.size,400)
L.insert(2,500)
print("삽입 x5",L)
L.delete(2)
print("삭제(2)",L)
L.delete(L.size-1)
print("삭제(3)",L)
L.delete(0)
print("삭제(0)",L)
L.replace(1, 300)
print("대체(1)",L)
L.insert(0,300)
print(L)
L.insert(1,300)
print(L)
L.insert(4,300)
print(L)
L.count(300)