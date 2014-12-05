import sys
w2w = {'Sunday': 0,
       'Monday': 1,
       'Tuesday': 2,
       'Wednesday': 3,
       'Thursday': 4,
       'Friday': 5,
       'Saturday': 6}

dd = [31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    m, d, w = rl().strip().split(" ")
    d = int(d) - w2w[w]
    m = int(m)
    if d <= 0:
        m = ((int(m) + 10) % 12 +1)
        d = dd[m-1] + d

    result = []
    for i in range(7):
        result.append(d)
        d = d+1
        if d > dd[m-1]:
            m = (m%12)+1
            d = 1

    print(" ".join(str(x) for x in result))
