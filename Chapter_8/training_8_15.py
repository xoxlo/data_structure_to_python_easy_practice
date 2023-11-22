def heappop(heap): # 최대 힙의 삭제 연산 함수
    size = len(heap) - 1 # 힙의 노드의 개수 (0번 인덱스 사용 X)
    if size == 0: # 노드의 개수가 없으면
        return None # 공백 힙
    pi = 1 # 부모 노드의 인덱스 위치
    i = 2 # 자식 노드의 인덱스 위치 (왼쪽 자식)
    root = heap[1] # 제일 위에 있는 노드(루트)를 삭제
    last = heap[size] # 마지막 노드
    
    while i <= size: # 더 내려갈 자식이 있을 때 까지 진행
        if i < size and heap[i] < heap[i+1]: # 오른쪽 자식이 더 크면
            i += 1 # down-heap 오른쪽 자식
        if last >= heap[i]: # 자식이 더 작으면 down-heap 종료
            break
        heap[pi] = heap[i] # 더 큰 자식을 부모 위치로 올림
        pi = i # 부모 위치가 자식 위치로 이동
        i *= 2 # 자식은 일단 부모의 왼쪽 자식
        
    heap[pi] = last # 맨 마지막 노드를 부모 위치에 복사
    heap.pop() # 맨 마지막 노드 삭제
    return root # 루트 반환