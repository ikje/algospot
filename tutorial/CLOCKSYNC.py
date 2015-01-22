import sys

switch = [[0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]]
switch_use = [0 for i in xrange(10)]

relate = []
for i in xrange(16):
    set = []
    for j in xrange(10):
        if i in switch[j]:
            set.append(j)
    relate.append(set)

rl = lambda: sys.stdin.readline()
n = int(rl())

map = []

def use(switch_no):
    for cn in switch[switch_no]:
        map[cn] = (map[cn] + 2) % 12 + 1

def set_twelve(clock_no, p, count):
    if clock_no >= 16:
        return count
    else:
        if p < len(relate[clock_no]):
            min = 1000
            switch_no = relate[clock_no][p]
            if switch_use[switch_no] == 0:
                # 0
                ret = set_twelve(clock_no, p+1, count)
                if min > ret:
                    min = ret
                # 1..3
                for i in xrange(3):
                    use(switch_no)
                    ret = set_twelve(clock_no, p+1, count+i+1)
                    if min > ret:
                        min = ret
                # 4
                use(switch_no)
            else:
                ret = set_twelve(clock_no, p+1, count)
                if min > ret:
                    min = ret

            return min
        else:
            if map[clock_no] == 12:
                for sn in relate[clock_no]:
                    switch_use[sn] += 1
                ret = set_twelve(clock_no + 1, 0, count)
                for sn in relate[clock_no]:
                    switch_use[sn] -= 1
                return ret
            else:
                return 1000

for i in xrange(n):
    map = [int(i) for i in rl().split()]

    ret = set_twelve(0,0,0)
    if ret > 100:
        ret = -1
    print( ret)
