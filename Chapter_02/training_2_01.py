def find_min_max(A):
    min = A[0]
    max = A[0]
    for i in range(1, len(A)):
        if max<A[i]: max = A[i]
        if min>A[i]: min = A[i]
    return min, max

data = [12, 3, 8, 4, 9, 1, 6, 2, 15]
x, y = find_min_max(data)
print("(min, max) -> ",(x,y))