import sys
import math

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    num = int(rl().strip())
    divisor = [1]

    p = 2
    while(p <= math.sqrt(num)):                
        if( num % p == 0):
            divisor.append(p)
            if( num/p > p ):
                divisor.append(int(num/p))
        p = p+1

    sum = 0
    for p in divisor:
        sum = sum + p

    if( sum <= num ):
        print("not weird")
    else:
        ds = sorted(divisor)
        ds.reverse()
        for p in ds:
            if( num - p >= 0 ):
                num = num - p

        if(num == 0):
            print("not weird")
        else:
            print("weird")