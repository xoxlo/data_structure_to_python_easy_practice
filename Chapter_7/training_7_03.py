from training_7_01 import printStep

def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if (A[j]>A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
        if not bChanged:
            break
    printStep(A, n-1)