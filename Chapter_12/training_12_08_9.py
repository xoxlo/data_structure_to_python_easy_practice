def quick_sort(A, left, right): # 퀵 정렬 함수
    if left < right: # 정렬 요소가 두 개 이상인 경우만 처리
        q = partition(A, left, right) # 피벗을 중심으로 두 부분으로 분할
        quick_sort(A, left, q-1) # 왼쪽 부분 리스트 정렬
        quick_sort(A, q+1, right) # 오른쪽 부분 리스트 정렬

def partition(A, left, right): # 피벗을 나누는 함수
    low = left + 1 # 왼쪽 부분 리스트의 인덱스 ( 오른쪽으로 증가 방향 )
    high = right # 오른쪽 부분 리스트의 인덱스 ( 왼족으로 감소 방향 )   
    pivot = A[left] # 피벗 설정
    while (low <= high):
        while low <= right and A[low] <= pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1
        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    return high