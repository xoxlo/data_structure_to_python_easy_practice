from training_4_02 import ArrayStack

def checkBrackets(statement): # stack에 {,},[,],(,) 를 저장하여 올바르게 괄호가 입력 되어있는지 확인
    stack = ArrayStack(100)
    for ch in statement:
        if ch == '{' or ch=='[' or ch=='(': # 검사 요소 ch 가 {, [, ( 라면
            stack.push(ch) # stack에 ch를 삽입
    
        elif ch == '}' or ch==']' or ch==')': # 검사 요소 ch 가 }, ], ) 라면
            if stack.isEmpty(): # 그리고 stack이 공백상태면
                return False # False 반환
            else: # 아니라면
                left = stack.pop() # stack에 있는 요소를 삭제 시킨 후 left에 저장
                
                if (ch=='}' and left != '{') or  \
                    (ch==']' and left != '[') or \
                    (ch==')' and left != '('):
                        return False # left에 있는 괄호와 짝이 안맞으면 False 반환
                    
    return stack.isEmpty() # stack에 아무것도 없으면 True 반환