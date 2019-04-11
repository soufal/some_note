import sys
n = int(input())
strList = []
for i in range(n):  
    tempStr = map(int,input().split())
    strList.extend(tempStr)
