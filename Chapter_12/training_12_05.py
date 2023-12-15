from training_12_03_4 import *

def heapSort(arr):
    n = len(arr)
    print("i=",0,arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
        print("i=",i,arr)
    print()
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        print("i=", i, arr)
        
arr = [71, 49, 92, 55, 38, 82, 72, 53]
heapSort(arr)