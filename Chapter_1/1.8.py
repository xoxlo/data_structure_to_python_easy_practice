# 다음 알고리즘의 시간 복잡도를 빅오 표기법으로 나타내라.

def algorithm1(n) :
    sum = 0
    for i in range(n):
        for j in range(i+1,n+1):
            sum = sum + j
            
# O(n^2)
# for문이 2개
# 첫번째 for문이 끝나고 두번째 for문을 반복
# 그러면 n*n 형태로 나오기 때문이다.
# 빅오 표기법은 최소 차수로 상한을 표시한다고 가정해야한다.