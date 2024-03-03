# 다음과 같은 순환적인 프로그램에서 sub(3)과 같이 호출할 때 함수 sub()가 호출되는 횟수는?

def sub(n):
    if n<=1:
        return n
    return sub(n-1)+sub(n+2)

# sub(3) -> 호출 - 1번
# sub(3) -> sub(2) , sub(1) 호출 - 2번
# sub(2) -> sub(1) , sub(0) 호출 - 2번
# 총 5번