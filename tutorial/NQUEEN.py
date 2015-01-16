import sys

ca = [0 for i in xrange(12) ]
cb = [0 for i in xrange(24) ]
cc = [0 for i in xrange(24) ]

def nqueen(line, n):
    if line == n:
        return 1

    sum = 0
    for i in xrange(n):
        if ca[i] == 0 and cb[line+i] == 0 and cc[line-i+n] == 0:
            ca[i] = 1
            cb[line+i] = 1
            cc[line-i+n] = 1
            sum += nqueen( line+1, n )
            ca[i] = 0
            cb[line+i] = 0
            cc[line-i+n] = 0

    return sum

rl = lambda: sys.stdin.readline()
n = int(rl())

for i in xrange(n):
    n = int(rl().strip())

    print( nqueen(0,n) )


