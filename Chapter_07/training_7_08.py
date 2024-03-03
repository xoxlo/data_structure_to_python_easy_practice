def binary_search(A, key, low, high): # 이진 탐색 알고리즘 (순환 구조)
    if (low > high):
        return -1
    
    middle = (low + high) // 2 # middle은 그 인덱스의 중간임
    
    if (key == A[middle]):
        return middle
    elif (key < A[middle]): # 키값이 middle 인덱스보다 크면 왼쪽에 있음
        return binary_search(A, key, low, middle - 1) # high -> middle -1
    else: # 키값이 middle 인덱스보다 작으면 오른쪽에 있음
        return binary_search(A, key, middle + 1, high) # low -> middle + 1