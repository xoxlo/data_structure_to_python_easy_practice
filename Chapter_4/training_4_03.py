from training_4_02 import ArrayStack
s = ArrayStack(100)

msg = input("문자열 입력 : ")
for c in msg:
    s.push(c)

print("문자열 출력 : ", end='')
while not s.isEmpty(): # 비어질 때 까지 반복
    print(s.pop(), end='')
print()