from copy import deepcopy

sol = [((20, 14), (6, 24), (12, 11)), ((16, 14), (6, 24), (12, 11)), ((16, 12), (6, 24), (12, 11)), ((12, 12), (6, 24), (12, 11)), ((12, 17), (6, 24), (12, 11)), ((12, 17), (6, 24), (17, 11)), ((12, 10), (6, 24), (17, 11)), ((12, 10), (6, 24), (12, 11)), ((12, 10), (6, 24), (12, 17)), ((14, 10), (6, 24), (12, 17)), ((14, 10), (6, 24), (12, 9)), ((12, 10), (6, 24), (12, 9)), ((12, 17), (6, 24), (12, 9)), ((12, 17), (6, 24), (18, 9)), ((12, 17), (6, 24), (18, 1)), ((12, 17), (6, 24), (13, 1)), ((12, 17), (6, 24), (13, 17)), ((12, 17), (6, 24), (18, 17)), ((12, 17), (6, 24), (18, 21)), ((12, 9), (6, 24), (18, 21)), ((18, 9), (6, 24), (18, 21)), ((18, 1), (6, 24), (18, 21)), ((4, 1), (6, 24), (18, 21)), ((4, 26), (6, 24), (18, 21)), ((1, 26), (6, 24), (18, 21)), ((1, 17), (6, 24), (18, 21)), ((18, 17), (6, 24), (18, 21)), ((18, 19), (6, 24), (18, 21)), ((11, 19), (6, 24), (18, 21)), ((11, 26), (6, 24), (18, 21)), ((14, 26), (6, 24), (18, 21)), ((14, 25), (6, 24), (18, 21)), ((6, 25), (6, 24), (18, 21)), ((6, 26), (6, 24), (18, 21)), ((6, 26), (14, 24), (18, 21)), ((6, 26), (14, 26), (18, 21)), ((6, 26), (11, 26), (18, 21)), ((6, 26), (11, 20), (18, 21)), ((6, 26), (18, 20), (18, 21)), ((6, 26), (18, 17), (18, 21)), ((6, 26), (18, 17), (9, 21)), ((6, 26), (18, 17), (9, 5)), ((6, 26), (12, 17), (9, 5)), ((6, 26), (12, 9), (9, 5)), ((6, 26), (18, 9), (9, 5)), ((6, 26), (18, 4), (9, 5)), ((6, 26), (18, 4), (1, 5)), ((6, 26), (1, 4), (1, 5)), ((6, 26), (1, 4), (1, 15)), ((6, 23), (1, 4), (1, 15)), ((6, 23), (10, 4), (1, 15))]

map = []
for y, l in enumerate(open('map').readlines()):
    map.append(list(l.strip().replace('s',' ').replace('b',' ')))

for s, b1, b2 in reversed(sol):
    mp = deepcopy(map)
    mp[s[1]][s[0]] = 's'
    mp[b1[1]][b1[0]] = 'b'
    mp[b2[1]][b2[0]] = 'b'
    print('\n'.join(''.join(l) for l in mp))
    input()
