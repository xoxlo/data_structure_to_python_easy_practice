def fib_1(n):
    if n == 0 or n == 1:
        return 1
    return fib_1(n-2) + fib_1(n-1)

def fib_2(n):
    a, b = 1, 1
    if n == 0 or n == 1:
        return 1
    for i in range(1, n):
        a, b = b, a+b
    return a