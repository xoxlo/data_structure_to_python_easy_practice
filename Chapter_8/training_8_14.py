def heappush(heap, n): # 최대 힙 삽인 연산 함수
    heap.append(n) # 
    i = len(heap) - 1
    while i != 1:
        pi = i//2
        if n <= heap[pi]:
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = n