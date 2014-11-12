import sys

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    v, t = rl().strip().split()
    v = float(v)
    rv = 0.00000
    rt = ""


    if t == "kg":
        rv = v * 2.2046
        rt = "lb"
    elif t == "l":
        rv = v * 0.2642
        rt = "g"
    elif t == "lb":
        rv = v * 0.4536
        rt = "kg"
    elif t == "g":
        rv = v * 3.7854
        rt = "l"

    print("%d %.4f %s" % (i+1, rv, rt))