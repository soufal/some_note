import sys
n = int(input())
strList = []
for line in sys.stdin:  
    tempStr = map(int,input().split())
    strList.extend(tempStr)
