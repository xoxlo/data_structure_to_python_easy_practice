# 다음 알고리즘의 시간 복잡도를 빅오 표기법으로 나타내라.

def algorithm1(n) :
    sum = 0
    for i in range(n):
        for j in range(i+1,n+1):
            sum = sum + j
            
# O(n^2)
# 첫번째 for문이 끝나고 두번째 for문을 반복
# 그러면 n*n 형태로 나오기 때문이다.
# 쉽게 생각해서 for문이 10개이면 n^10 이런 식으로 생각하면 된다. 
# 빅오 표기법은 최소 차수로 상한을 표시한다고 가정해야한다.

# 추가로 for문에서 n번 연산 -> 다음 for문에서 n+1 까지 연산
# 고로 최소 차수로 나타내면 n^2 형태

def algorithm2(n):
    k = 0
    while n>1:
        n = n/2
        #k++ # 파이썬에서는 ++ 안되니까 k+=1로 변경
        k+=1
    return k
# O(n)
# while문 안에서 최대로 n번 시간이 걸린다.
# ..