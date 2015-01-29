import sys

dist = []
visit = []
size = 0
min = 0

def calcTSP( cur, visit_cnt, sum ):
    global min
    if visit_cnt == size:
        if min > sum:
            min = sum
    else:
        visit[cur] = 1
        for i in xrange(size):
            if visit[i] == 0:
                cur_min = sum + dist[cur][i]
                if min > cur_min:
                    calcTSP( i, visit_cnt+1, cur_min )
        visit[cur] = 0

rl = lambda: sys.stdin.readline()
n = int(rl())
for c in range(n):
    size = int(rl())

    min = 20000
    dist = []
    visit = []
    for y in xrange(size):
        line = [float(i) for i in rl().split()]
        dist.append(line)
        visit.append(0)

    for i in xrange(size):
        calcTSP( i, 1, 0.0)

    print("{0:.10f}".format(min))
