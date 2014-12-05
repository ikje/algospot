import sys
import math
from Queue import Queue

dx = [0,1,0,-1]
dy = [1,0,-1,0]


result = [[4 for x in xrange(50)] for y in xrange(50)]

def reachThree(map, nx, ny, sx, sy):
    for y in xrange(ny):
        for x in xrange(nx):
            result[y][x] = 4
    result[sy][sx] = 0


    q = Queue()
    q.put((sx,sy))
    while( not q.empty() ):
        cx, cy = q.get()
        cc = result[cy][cx] + 1

        for cd in xrange(4):
            tx = cx
            ty = cy
            while(True):
                tx = tx + dx[cd]
                ty = ty + dy[cd]

                if tx < 0 or ty < 0 or tx >= nx or ty >= ny:
                    break

                if map[ty][tx] == '.':
                    #road
                    if(result[ty][tx] != 4):
                        continue

                    result[ty][tx] = cc
                    if result[ty][tx] < 3:
                        q.put((tx,ty))
                    pass
                else:
                    #wall
                    result[ty][tx] = cc
                    break;


    count = 0    
    for y in xrange(ny):
        #print("".join(str(x) for x in result[y]))
        for x in xrange(nx):
            if map[sy][sx] == map[y][x] and result[y][x] <= 3:
                count = count + 1

    return int(count-1)

rl = lambda: sys.stdin.readline()
n = int(rl())
for c in range(n):
    row, column = rl().strip().split()
    row = int(row)
    column = int(column)
    
    map = []    
    for y in xrange(row):
        line = rl().strip()
        map.append(line)                

    rc = 0
    for y in xrange(row):
        for x in xrange(column):
            if (map[y][x] != '.' ):
                t = reachThree(map, column, row, x, y)
                #print("%d %d => %d" % (i,j,t))
                rc = rc + t

    print(int(rc/2))


'''
rl = lambda: sys.stdin.readline()
n = int(rl())
for c in range(n):
    ny, nx = rl().strip().split()
    ny = int(ny)
    nx = int(nx)

    map = []    
    for y in xrange(ny):
        line = rl().strip()
        map.append(line)

    tiles = {}
    graph = {}

    for y in xrange(ny):
        for x in xrange(nx):            
            sp = y * nx + x

            if map[y][x] != '.':
                tile = map[y][x]
                if not (tile in tiles):
                    tiles[tile] = []
                tiles[tile].append(sp)

            graph[sp] = {}
            for d in xrange(4):                
                ty = y
                tx = x
                while(True):
                    ty = ty + dy[d]
                    tx = tx + dx[d]

                    if tx < 0 or ty < 0 or tx >= nx or ty >= ny:
                        break

                    tp = ty * nx + tx
                    if map[ty][tx] == '.':                
                        graph[sp][tp] = 1
                    else:
                        graph[sp][tp] = 1
                        break

    result_count = 0
    for tile, ps in tiles.iteritems():
        for i in range(0,len(ps)):
            for j in range(i+1, len(ps)):
                find = False
                sp = ps[i]
                ep = ps[j]

                if ep in graph[sp]:
                    result_count = result_count + 1
                    continue

                for t1 in graph[sp].keys():
                    if ep in graph[t1]:
                        result_count = result_count + 1
                        find = True
                        break;
                    for t2 in graph[t1].keys():
                        if ep in graph[t2]:
                            result_count = result_count + 1
                            find = True
                            break;
                    if(find):
                        break;

    print(result_count)
'''