import sys

word2num = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
num2word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    a, op, b, eq, result = rl().strip().split()
    a = word2num[a]
    b = word2num[b]
    v = 0

    if op == "+":
        v = a+b
    elif op == "-":
        v = a-b
    else:
        v = a*b

    if v < 0 or v >= 10 or sorted(num2word[v]) != sorted(result):
        print("No")
    else:
        print("Yes")