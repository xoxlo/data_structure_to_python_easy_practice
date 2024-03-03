def calc_height(n): # 이진트리의 높이 계산 함수
    if n is None: # 공백 트리 -> 0 반환
        return 0
    hLeft = calc_height(n.left) # 왼쪽트리의 높이
    hRight = calc_height(n.right) # 오른쪽트리의 높이
    if (hLeft > hRight): # 높이는 좌,우 어느 곳이든 상관없으니까 더 높은 트리에다가 +1을 해주면서 반환
        return hLeft + 1
    else:
        return hRight + 1

def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right)