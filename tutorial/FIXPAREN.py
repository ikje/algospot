import sys

opens = {
    ')':'(',
    '}':'{',
    ']':'[',
    '>':'<'
    }
closes = {
    '(':')',
    '{':'}',
    '[':']',
    '<':'>'
    }

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    seq, ps = rl().strip().split()

    priority = {}
    for i in range(4):
        priority[ps[i]] = i
        
    st = []
    result = []
    for c in seq:
        if c in "({[<":
            st.append(c)
            result.append("")
        else:            
            open = st.pop()
            close = c
            if c != open:
                if priority[open] < priority[opens[c]]:
                    close = closes[open]
                else:
                    open = opens[c]

            tmp =""
            t = result.pop()
            while t != "":
                tmp = t + tmp
                t = result.pop()
                
            tmp = open + tmp + close
            result.append(tmp)

    print("".join(result))