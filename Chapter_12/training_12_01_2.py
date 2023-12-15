def sortGapInsertion(A, first, last, gap): # 셸 정렬에서 사용되는 삽입 정렬
    for i in range(first+gap, last+1, gap): # 리스트의 요소를 gap만큼 건너뛰면서 삽입
        key = A[i] # 
        j = i - gap
        while j >= first and key < A[j]:
            A[j+gap] = A[j]
            j = j - gap
        A[j+gap] = key

def shell_sort(A):
    n = len(A)
    gap = n//2
    while gap > 0:
        if(gap%2) == 0:
            gap += 1
        for i in range(gap):
            sortGapInsertion(A, i, n-1, gap)
        print('     Gap = ',gap, A)
        gap = gap//2
        
list = [5,3,8,4,9,1,6,2,7]

print("Original   : ",list)
shell_sort(list)
print("Shell      : ",list)