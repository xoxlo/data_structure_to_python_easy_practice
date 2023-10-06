# 다음 함수에서 asterisk(5)와 같이 호출할 때 출력되는 *의 개수는?

def asterisk(i):
    if i>1:
        asterisk(i/2)
        asterisk(i/2)
    print("*",end='')

asterisk(5)