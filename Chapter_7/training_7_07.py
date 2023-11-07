def sequential_search(A, key, low, high): # 순차 탐색
    for i in range(low, high+1): # low번째부터 high 까지 비교
        if A[i] == key : # key값이 i번째 레코드와 같으면
            return i # 그 레코드 반환
    return -1