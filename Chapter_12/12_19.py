def is_sorted(A): # 오름차순으로 정렬되어 있는지 검사하는 함수
    n = len(A) # A 리스트의 길이를 가져옴
    for i in range(1, n): # 리스트의 길이 만큼 반복
        if A[i-1] > A[i]: # 앞에 있는 값이 뒤에 있는 값이 더 크면
            return False # False반환 오름차순이 아님
    return True # True 오름차순