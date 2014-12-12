import sys

ca = []
cb = []
cc = []

def nqueen(line, n):
    for i in xrange(n):
        if ca[i] == 0 and cb[line+i] == 0 and cc[n+line-i]

rl = lambda: sys.stdin.readline()
n = int(rl())

for i in range(n):
    n = int(rl().strip())



    priority = {}
    for i in range(4):
        priority[ps[i]] = i
        
    st = []
    result = ""
    tmp = ""
    for c in seq:
        if c in "({[<":
            st.append(c)
        else:            
            open = st.pop()
            if c != open:
                if priority[open] < priority[opens[c]]:
                    tmp = open + tmp + closes[open]
                else:
                    tmp = opens[c] + tmp + c
            else:
                tmp = open + tmp + c
            if len(st) <= 0:
                result = result + tmp
                tmp = ""
    result = result + tmp

    print(result)