from heapq import *

g = {} 
bs = []
s = None
for y, l in enumerate(open('map').readlines()):
    for x, c in enumerate(l.strip()):
        if c == 's':
            s = (x,y)
            g[(x,y)] = ' '
        elif c == 'b':
            bs.append((x,y))
            g[(x,y)] = ' '
        else:
            g[(x,y)] = c

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
def slide(p, d, os):
    if (p[0]-d[0], p[1]-d[1]) in os:
        return p
    while True:
        pn = (p[0]+d[0], p[1]+d[1])
        if g[pn] == '#' or pn in os:
            return p
        p = pn

# need pq, need scoring function. a*? try bfs first
state = (s, bs[0], bs[1])
q = [[state]] # TODO record moves
dists = {}
while len(q) > 0:
    path = q.pop(0)
    cur = path[0]
    if cur not in dists or dists[cur] > len(path):
        dists[cur] = len(path)
    else:
        continue
    if g[cur[0]] == 'g':
        print('win!')
        print(path)
        break
    for d in dirs:
        c = slide(cur[0], d, cur[1:])
        if c != cur[0]:
            q.append([(c, cur[1], cur[2])] + path)
        c = slide(cur[1], d, [cur[0],cur[2]])
        if c != cur[1]:
            q.append([(cur[0], c, cur[2])] + path)
        c = slide(cur[2], d, cur[:2])
        if c != cur[2]:
            q.append([(cur[0], cur[1], c)] + path)


print('done??')
#print(dists)



