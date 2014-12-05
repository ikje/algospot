import sys

rl = lambda: sys.stdin.readline()
n = int(rl())
for i in range(n):
    bs = rl().strip()
    result = True
    s = []
    for b in bs:
        if b == '(' or b == '[' or b == '{':
            s.append(b)
        else:
            if len(s) <= 0:
                result = False
                break
            ss = s.pop()
            if b == ')' and ss != '(':
                result = False
                break
            elif b == '}' and ss != '{':
                result = False
                break
            elif b == ']' and ss != '[':
                result = False
                break

    if len(s) > 0:
        result = False
                  
    if result == True:
        print("YES")
    else:
        print("NO")
