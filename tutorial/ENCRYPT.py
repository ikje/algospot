import sys
rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
	str = rl().strip()
	two = ""
	one = ""
	for j in range(len(str)):
		if j%2 == 0:
			two = two + str[j]
		else:
			one = one + str[j]
	print(two + one)
		