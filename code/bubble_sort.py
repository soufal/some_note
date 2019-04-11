#! /usr/bin/env python3


def bubble(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


#k = [1,5,9,10,2]
k = list(map(int, input().split()))
result = bubble(k)
print(result)
