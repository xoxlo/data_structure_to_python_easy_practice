from training_7_01 import printStep

def insertion_sort(A): # 삽입 정렬
    n = len(A)
    for i in range(1, n): # 인덱스 1 ~ n까지
        key = A[i] # i번째 인덱스를 key로
        j = i-1 # key를 바로 앞 인덱스랑 비교 하려고 j 사용
        while j >=0 and A[j] > key: # key값이 선택된 인덱스보다 작으면
            A[j + 1] = A[j] # key값보다 큰 요소를 한 칸씩 뒤로 이동
            j -= 1 # 0이 될 때까지 반복
        A[j + 1] = key # key값을 한칸씩 뒤로 변경
        printStep(A, i)
