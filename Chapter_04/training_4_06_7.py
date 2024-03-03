from training_4_02 import ArrayStack

def precedence (op):                        # 연산자의 우선순위 반환
    if op == '(' or op == ')': return 0     # 괄호를 가장 낮게 처리
    elif op == '+' or op == '-': return 1   # +, -의 우선순위
    elif op == '*' or op == '/': return 2   # *, /가 가장 높음.
    else:
        return -1
    
def Infix2Postfix(expr):                    # 중위표기 수식 -> 후위표기 수식으로 변환
    s = ArrayStack(100)
    output = []
    
    for term in expr:
        if term in '(':
            s.push('(')
            
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
                    
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if ( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else:
                    break
            s.push(term)

        else:
            output.append(term)
            
    while not s.isEmpty():
        output.append(s.pop())
        
    return output