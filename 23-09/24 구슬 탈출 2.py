# https://www.acmicpc.net/problem/13460

import sys
from collections import defaultdict

inp = sys.stdin.readline

N, M = map(int, inp().split())
chart = []
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]
red = None
blue = None
min_val = float('inf')
visited_cnt = defaultdict(lambda: float('inf'))

for i in range(N):
    raw = inp().rstrip()
    j = raw.find('R')
    if j != -1:
        red = (i, j)
        raw = raw.replace('R', '.')
    j = raw.find('B')
    if j != -1:
        blue = (i, j)
        raw = raw.replace('B', '.')
    chart.append(raw)

def move(this, other, dx, dy): # 구멍에 빠지는지 여부와 최종 위치를 반환
    x, y = this
    met_other = False
    
    while True:
        x += dx
        y += dy
        if not (0 <= x < N and 0 <= y < M):
            break
        if (x, y) == other:
            met_other = True
        val = chart[x][y]
        if val == 'O':
            return (True, None)
        if val == '#':
            break
        
    x -= dx
    y -= dy
    if met_other:
        x -= dx
        y -= dy
        
    return (False, (x, y))
    
def dfs(cnt, red, blue, success):
    global min_val
    if cnt >= min_val:
        return
    if success:
        min_val = cnt
        return
    elif cnt == 10:
        return
    
    if visited_cnt[((red, blue))] <= cnt:
        return
    visited_cnt[((red, blue))] = cnt
    
    for k in range(4):
        red_suc, red_pos = move(red, blue, dxs[k], dys[k])
        blue_suc, blue_pos = move(blue, red, dxs[k], dys[k])
        if blue_suc:
            continue
        dfs(cnt + 1, red_pos, blue_pos, red_suc)

dfs(0, red, blue, False)
if min_val == float('inf'):
    print(-1)
else:
    print(min_val)