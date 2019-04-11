#! /usr/bin/env python3
class name_score():
    def __init__(self,name,score):
        self.name = name
        self.score = score

def bubble(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i].score > arr[j].score:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


#k = [1,5,9,10,2]
N = int(input())
for i in range(N):
    self.score_name.name, self.score_name.score = input().split()

result = bubble(score_name)
print(result)
