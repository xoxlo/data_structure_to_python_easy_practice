def binary_search(A, key, low, high):
    while(low <= high): # 탐색할 항목이 하나 이상
        middle = (low + high) // 2
        
        if key == A[middle]:
            return middle
        elif (key > A[middle]): # key가 middle 인덱스보다 크면 오른쪽에 있다는 뜻
            low = middle + 1 # low를 middle + 1해서 변겅 -> low가 middle + 1로 변경, high는 그대로. 범위가 줄어듦
        else: # key가 middle 인덱스보다 작으면 왼쪽에 있다는 뜻
            high = middle - 1 # high를 middle - 1해서 변경 -> low는 그대로, high는 middle -1로 변경되면서 범위가 줄어듦
    return -1 # low와 high가 역전이 되면 찾는 값이 없다는 것, 그래서 -1 반환