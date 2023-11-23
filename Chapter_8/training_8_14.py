def heappush(heap, n): # 최대 힙 삽인 연산 함수
    heap.append(n) # n을 리스트 heap의 맨 뒤에 삽입
    i = len(heap)-1 # n이 삽입된 위치 (자식 위치)
    while i != 1: # 루트까지 올라가지 않았으면 계속 반복
        pi = i//2 # 부모의 노드의 위치
        if n <= heap[pi]: # 부모보다 작으면
            break # 반복문 종료
        heap[i] = heap[pi] # 부모와 자식을 바꿈
        i = pi # i가 부모위치로 올라감
    heap[i] = n # 마지막 위치에 n 산입