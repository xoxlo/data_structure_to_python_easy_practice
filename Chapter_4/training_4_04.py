from training_4_02 import ArrayStack

def checkBrackets(statement): # stack에 {,},[,],(,) 를 저장하여 올바르게 괄호가 입력 되어있는지 확인
    stack = ArrayStack(100)
    jo_geon = None
    line_number = 1 # 현재 라인 번호
    char_number = 1 # 현재 문자 위치

    for ch in statement:
        if ch == '\n':
            line_number += 1
            char_number = 1
        else:
            char_number += 1
            
        if ch == '{' or ch == '[' or ch == '(': # 검사 요소 ch 가 {, [, ( 라면
            stack.push(ch) # stack에 ch와 index(오류 발생시 어디서 발생했는지 확인 하기 위함)를 삽입
            
        elif ch == '}' or ch == ']' or ch == ')':
            if stack.isEmpty(): # stack이 공백상태 - 여는 괄호 < 닫는 괄호
                jo_geon = 1 # 조건1 위반 - 닫는 괄호가 더 많음
                break
            else:
                left = stack.pop() # 스택에서 가장 최근에 추가한 요소를 가져옴
                if (ch == '}' and left != '{') or \
                   (ch == ']' and left != '[') or \
                   (ch == ')' and left != '('):
                    jo_geon = 3 # 조건3 위반 - 괄호 짝이 안맞음.
                    break

    if jo_geon == 1:
        return (1, line_number, char_number)  # 조건 1 위반: 닫는 괄호가 너무 많음
    elif jo_geon == 3:
        return (3, line_number, char_number)  # 조건 3 위반: 괄호 짝이 맞지 않음
    
    if not stack.isEmpty():
        left = stack.pop()
        return (2, line_number, char_number)  # 조건 2 위반: 여는 괄호가 너무 많음

    return (0, 0, 0)

# 테스트
if __name__ == "__main__":
    statement = input("괄호를 검사할 표현식을 입력하세요: ")
    result = checkBrackets(statement)
    if result[0] == 0:
        print('괄호 매칭 성공')
    else:
        error_code, line_number, char_number = result
        print("입력한 괄호 --> ",statement)
        print(f"( 조건{error_code} 위반, 라인: {line_number}, 문자 위치: {char_number})")