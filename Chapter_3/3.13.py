def merge(self, setB):
    setC = []
    i = 0  # 집합 A의 인덱스
    j = 0  # 집합 B의 인덱스

    while i <  len(self) and j < len(setB): # 집합A, 집합B의 원소 만큼 반복
        if self[i] < setB[j]: # 집합B가 집합A보다 크면
            setC.append(self[i]) # 집합C에다가 집합A의 원소를 저장
            i += 1
        else:
            setC.append(setB[j]) # 집합B가 집합A보다 작으면 집합B의 원소를 저장
            j += 1
            
    # 위 반복은 오름차순으로 정렬해주는 것.
    
    setC.extend(self[i:])  # 남은 원소를 추가
    setC.extend(setB[j:])

    return setC