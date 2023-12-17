# 코드 실습 1.1

def sortGapInsertion(A, first, last, gap): # 셸 정렬에서 사용되는 삽입 정렬
    for i in range(first+gap, last+1, gap): # 리스트의 요소를 gap만큼 건너뛰면서 반복
        key = A[i] # 
        j = i - gap
        while j >= first and key < A[j]: # 삽입 위치 찾음
            A[j+gap] = A[j] # gap만큼 건너뛰면서 저장
            j = j - gap
        A[j+gap] = key


# 코드 실습 1.2

def shell_sort(A):
    n = len(A)
    gap = n//2 # 최초의 gap -> 리스트 크기 절반
    while gap > 0: # gap이 0 이상이면
        if(gap%2) == 0: # gap이 짝수이면
            gap += 1 # +1을 함
        for i in range(gap):
            sortGapInsertion(A, i, n-1, gap)
        print('     Gap = ',gap, A)
        gap = gap//2 # gap을 반으로 줄임
        
list = [5,3,8,4,9,1,6,2,7]

print("Original   : ",list)
shell_sort(list)
print("Shell      : ",list)