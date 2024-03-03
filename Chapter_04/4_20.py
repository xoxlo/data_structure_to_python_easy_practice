from training_4_02 import ArrayStack
from training_4_05 import evalPostfix # 후위표기식 연산
from training_4_06_7 import Infix2Postfix, precedence # 중위표기식 -> 후위표기식으로 변환, 그리고 우선순위 결정

# 4.20
# 4.4절의 코드를 수정하여 사용자로부터 직접 중위표기 수식을 입력 받아 이를 처리하여
# 결과를 출력하는 프로그램을 작성하라. 단, 입력 처리의 간소화를 위해 수식의 연산자
# 와 피연산자는 모두 공백으로 분리하여 입력한다고 가정하자. 입력과 실행 에는 다음과 같다.

str = input("입력 수식 (공백문자로 분리) = ").split() # split를 이용해 공백으로 분리
post_str_fix = Infix2Postfix(str)
result_str = evalPostfix(post_str_fix)
print(' 중위 표기 -> ',str)
print(' 후위 표기 -> ',post_str_fix)
print(' 계산값 -> ',result_str)