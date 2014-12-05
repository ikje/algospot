import sys

# 1st = 1,3,5,7 xor 0
# 2st = 2,3,6,7 xor 0
# 4th = 4,5,6,7 xor 0
rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    bits = []
    for i in rl().strip():
        bits.append(int(i))
    c1 = (bits[0] + bits[2] + bits[4] + bits[6]) % 2
    c2 = (bits[1] + bits[2] + bits[5] + bits[6]) % 2
    c3 = (bits[3] + bits[4] + bits[5] + bits[6]) % 2

    syndrom = c3*4 + c2*2 + c1
    if(syndrom != 0):
        syndrom = syndrom - 1
        bits[syndrom] = (bits[syndrom] + 1)%2    
    print("%d%d%d%d" % (bits[2], bits[4], bits[5], bits[6]))

