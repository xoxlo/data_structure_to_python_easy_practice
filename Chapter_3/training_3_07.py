from training_3_06 import *

setA = ArraySet()
setA.insert('아이폰20 프로')
setA.insert('애플워치 초울트라')
setA.insert('나이키 신발')
print('Set A : ',setA)

setB = ArraySet()
setB.insert('아이패드')
setB.insert('아이폰20 프로')
setB.insert('반지')
setB.insert('에어팟 프로')
print('Set B : ',setB)

setA.delete('나이키 신발')
setA.delete('아디다스 신발')
print('Set A : ',setA)
setB.insert('반지')
print('Set B : ',setB)

print('A U B : ',setA.union(setB))
print('A ^ B : ',setA.intersect(setB))
print('A - B : ',setA.difference(setB))