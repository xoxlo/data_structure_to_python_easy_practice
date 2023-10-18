from training_4_02 import ArrayStack

def evalPostfix( expr ):
    s = ArrayStack(100)
    
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'):
                s.push(val1 + val2)
            elif (token == '-'):
                s.push(val1 - val2)
            elif (token == '*'):
                s.push(val1 * val2)
            elif (token == '/'):
                s.push(val1 / val2)
        else:
            s.push(float(token))
            
    return s.pop()

expr1 = ['4','2','/','3','-','6','7','+','*']
expr2 = ['5','2','/','3','5','8','*','8','+']
print(expr1, '-->', evalPostfix(expr1))
print(expr2, '-->', evalPostfix(expr2))