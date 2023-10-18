from training_4_02 import ArrayStack
def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch == '{' or ch=='[' or ch=='(':
            stack.push(ch)
    
        elif ch == '}' or ch==']' or ch==')':
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch=='}' and left != '{') or \
                    (ch==']' and left != '[') or \
                    (ch==')' and left != '('):
                        return False
                    
    return stack.isEmpty()



s1 = " { A[i+1] = 0;}                "
s2 = " if((i=='안호영') && (j=='송창석')"
s3 = " A[ ( i + 1 } ) ] = 0          "
print(s1, " ---> ", checkBrackets(s1))
print(s2, " ---> ", checkBrackets(s2))
print(s3, " ---> ", checkBrackets(s3))