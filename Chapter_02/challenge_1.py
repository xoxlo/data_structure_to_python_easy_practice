# 1부터 n까지의 자연수의 합을 구해 반환하는 함수 sum_iter(n)을 for문을 이용해 작성하라.
def sum_iter(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

# 위 문제의 함수르 반복이 아니라 순한을 이용해 함수 sum_recur(n)을 작성하라.
def sum_recur(n):
    if n <= 1:
        return n
    else:
        return n + sum_recur(n-1)