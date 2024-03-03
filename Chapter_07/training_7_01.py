def selection_sort(A) : # 선택 정렬 A는 리스트임.
    n = len(A) # 리스트 A의 길이를 n에다가 저장
    for i in range(n-1): # n-1 만큼 반복 (외부루프)
        least = i;
        for j in range(i+1, n): # i+1부터 n까지 반복 (내부루프)
            if (A[j]<A[least]): # 최솟값보다 작을 떄
                least = j # j를 least로 갱신
        A[i], A[least] = A[least], A[i] # 배열 교환
        printStep(A, i+1)
        
def printStep(arr, val):
    print(" Step %2d = " % val, end='')
    print(arr)