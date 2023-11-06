from training_7_01 import printStep

def bubble_sort(A): # 버블 정렬
    n = len(A)
    for i in range(n-1, 0, -1): # 인덱스 n-1부터 0까지 비교 한다는 뜻
        bChanged = False
        for j in range(i): # i만큼 반복
            if (A[j]>A[j+1]): # 앞에 인덱스가 뒤에 인덱스보다 크면
                A[j], A[j+1] = A[j+1], A[j] # 둘이 서로 교환
                bChanged = True
        if not bChanged:
            break
        printStep(A, n-i);