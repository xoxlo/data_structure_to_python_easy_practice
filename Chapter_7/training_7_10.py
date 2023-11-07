def interpolation_search(A, key, low, high): # 보간 탐색
    if (low > high):
        return -1
    
    middle = int(low + (high-low) * (key-A[low].key) / (A[high].key-A[low].key)) # 탐색 위치가 킷값이 있는 곳에 근접하도록 가중치를 줌
    
    if (key == A[middle]):
        return middle
    elif (key < A[middle]): # 키값이 middle 인덱스보다 크면 왼쪽에 있음
        return interpolation_search(A, key, low, middle - 1) # high -> middle -1
    else: # 키값이 middle 인덱스보다 작으면 오른쪽에 있음
        return interpolation_search(A, key, middle + 1, high) # low -> middle + 1