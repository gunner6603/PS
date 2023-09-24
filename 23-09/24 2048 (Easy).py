# https://www.acmicpc.net/problem/12100

import sys

inp = sys.stdin.readline

def dfs(cnt, block):
    if cnt == 5:
        return max(max(row) for row in block)
    
    def move(flipped):
        N = len(flipped)
        result = []
        
        for row in flipped:
            filtered_row = [elem for elem in row if elem != 0]
            new_row = []
            
            while filtered_row:
                if len(filtered_row) >= 2 and filtered_row[-2] == filtered_row[-1]:
                    new_row.append(filtered_row.pop() + filtered_row.pop())
                else:
                    new_row.append(filtered_row.pop())

            while len(new_row) < N:
                new_row.append(0)
                
            result.append(new_row)
        
        return result
    
    # 하
    flipped1 = [list(row) for row in zip(*block)]
    # 상
    flipped2 = [list(reversed(row)) for row in flipped1]
    # 좌
    flipped3 = [list(reversed(row)) for row in block]
    # 우
    flipped4 = [row[:] for row in block]
    
    max_val = 0
    
    for flipped in [flipped1, flipped2, flipped3, flipped4]:
        moved = move(flipped)
        max_val = max(max_val, dfs(cnt + 1, moved))
    
    return max_val

N = int(inp())
block = []
for _ in range(N):
    block.append(list(map(int, inp().split())))
print(dfs(0, block))