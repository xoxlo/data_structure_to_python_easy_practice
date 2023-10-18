from training_4_02 import ArrayStack

def evalPostfix( expr ):
    s = ArrayStack(100)
    
    for token in expr:
        if token in "+-*/": # '+' or '-' or '*' or '/' 와 같은 말
            
            val2 = s.pop() # 피연산자2
            val1 = s.pop() # 피연산자1
            
            ## 토큰이 연산자인 경우
            # 피연산자를 두개 꺼내고, 연산자에 맞는 연산 후 s에 저장
            if (token == '+'):
                s.push(val1 + val2) 
            elif (token == '-'):
                s.push(val1 - val2)
            elif (token == '*'):
                s.push(val1 * val2)
            elif (token == '/'):
                s.push(val1 / val2)
        else:
            s.push(float(token)) # 토큰이 연산자가 아닌 경우 실수로 변환 후 s에 저장
            
    return s.pop() # 최종결과가 스택에 저장되서 마지막 결과값 반환

# expr1 = ['4','2','/','3','-','6','7','+','*']
# expr2 = ['5','2','/','3','5','8','*','8','+']
# print(expr1, '-->', evalPostfix(expr1))
# print(expr2, '-->', evalPostfix(expr2))