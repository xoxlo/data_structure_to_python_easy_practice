from training_4_02 import ArrayStack
from training_4_05 import evalPostfix
from training_4_06_7 import Infix2Postfix, precedence

infix1 = ['4','/','2','-','3','*','6','+','7']
infix2 = ['5','/','5','-','4','*','2','+','6']
postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)

print(' 중위 표기 -> ',infix1)
print(' 후위 표기 -> ',postfix1)
print(' 계산값 -> ',result1)
print(' 중위 표기 -> ',infix2)
print(' 후위 표기 -> ',postfix2)
print(' 계산값 -> ',result2)
