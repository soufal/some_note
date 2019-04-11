import sys
n = int(input()) * 2
time = 2 * 60
strList = []
it_time = []
it_score = []
for i in range(n):  
	tempStr = input().split()
	strList.append(tempStr)
for j in strList:
	it_time.append(int(strList[i][0]))
	it_time.append(int(strList[i][2]))
	it_score.append(int(strList[i][1]))
	it_score.append(int(strList[i][3]))

x = [False for raw in range(n)]
v = 0

optp = [[0 for col in range(time + 1)] for raw in range(n)]
def final_score(w, p, n, time, x):
    for i in range(1, n):
        for j in range(1, time + 1):
            optp[i][j] = optp[i - 1][j]
            if (j >= w[i]) and (optp[i - 1][j - w[i]] + p[i] > optp[i - 1][j]):
                optp[i][j] = optp[i - 1][j - w[i]] + p[i]
    
    j = time
    for i in range(n, 0, -1):
        if optp[i][j] > optp[i - 1][j]:
            x[i] = True
            j = j - w[i]  
    
    v = optp[n][time]
    return v
sys.stdout.write(str(final_score(it_time, it_score, n, time, x)))

