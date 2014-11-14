import sys

encodings = {
    "%20":" ",
    "%21":"!",
    "%24":"$",
    "%28":"(",
    "%29":")",
    "%2a":"*"
    }

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    s = rl().strip()

    for key, value in encodings.items():
        s = s.replace(key,value)

    s = s.replace("%25","%")

    print(s)