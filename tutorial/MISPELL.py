import sys
rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
	p, s = rl().strip().split(" ")
	p = int(p)
	print str(i+1) + " " + s[:p-1] + s[p:]