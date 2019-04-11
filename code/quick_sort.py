#! /usr/bin/env python3

def quicksort(arr, begin, end):
    if begin > end:
        return
    temp = arr[begin]
    i, j = begin, end
    while i != j :
        while arr[j]>=temp and i < j:
            j -= 1
        while arr[i]<=temp and i < j:
            i += 1
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[begin], arr[i] = arr[i], temp
    quicksort(arr, begin, i-1)
    quicksort(arr, i+1, end)
    return arr

arr = list(map(int, input().split()))
print(quicksort(arr, 0, len(arr) - 1))
