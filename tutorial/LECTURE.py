import sys
rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    str = rl().strip()
    array = [ str[j:j+2] for j in range(0, len(str), 2) ]
    array.sort()
    print( "".join(array) )