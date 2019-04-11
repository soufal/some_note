import sys
N, M = input().split()
N = int(N)
M = int(M)
max_value = max(N, M)
min_value = max(N, M)
if M >= 2 * N:
	sys.stdout.write(str(N))
if 2 * N > M and M >= N:
	sys.stdout.write(str(N+M) / 3))
