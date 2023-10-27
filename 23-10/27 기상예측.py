# https://www.acmicpc.net/problem/1200

import sys

inp = sys.stdin.readline

N, M, R, S = map(int, inp().split())
chart = [list(map(int, inp().split())) for _ in range(N)]
acc = [[0]*M for _ in range(N)] # 누적합

for i in range(N):
    row_acc = 0
    for j in range(M):
        row_acc += chart[i][j]
        if i == 0:
            acc[i][j] = row_acc
        else:
            acc[i][j] = acc[i - 1][j] + row_acc

permutations = []
tmp_permutation = []

def dfs(last, cur):
    if cur == S:
        tmp_permutation.append(M - 1)
        permutations.append(tmp_permutation[:]) # append copy
        tmp_permutation.pop()
        return
    for i in range(last + 1, M - (S - cur)):
        tmp_permutation.append(i)
        dfs(i, cur + 1)
        tmp_permutation.pop()

dfs(-1, 0)

def pre_verify(permutation, threshold):
    for i in range(len(permutation)):
        upper_col_idx = permutation[i]
        lower_col_idx = permutation[i - 1] + 1 if i > 0 else 0
        square_sum = acc[-1][upper_col_idx] - (acc[-1][lower_col_idx - 1] if lower_col_idx > 0 else 0)
        if (square_sum + R) // (R + 1) > threshold:
            return False
    return True

def verify(permutation, threshold):
    lower_row_idx = 0
    for _ in range(R + 1): # 가로 방향으로는 총 (R+1)개의 chunk로 나눠져야 함 
        for upper_row_idx in range(N - 1, lower_row_idx - 1, -1):
            suc = True
            for i in range(len(permutation)):
                upper_col_idx = permutation[i]
                lower_col_idx = permutation[i - 1] + 1 if i > 0 else 0
                square_sum = acc[upper_row_idx][upper_col_idx]  \
                            - (acc[upper_row_idx][lower_col_idx - 1] if lower_col_idx > 0 else 0) \
                            - (acc[lower_row_idx - 1][upper_col_idx] if lower_row_idx > 0 else 0) \
                            + (acc[lower_row_idx - 1][lower_col_idx - 1] if lower_row_idx > 0 and lower_col_idx > 0 else 0)
                if square_sum > threshold:
                    suc = False
                    break
            if suc:
                lower_row_idx = upper_row_idx + 1
                break
        if lower_row_idx == N:
            return True
    return False

left = acc[-1][-1] // ((R + 1)*(S + 1))
right = min(2_000_000 * 9 * 9, acc[-1][-1])
                    
while left <= right:
    mid = (left + right) // 2
    suc = False
    for permutation in permutations:
        if not pre_verify(permutation, mid):
            continue
        if verify(permutation, mid):
            suc = True
            break
    if suc:
        right = mid - 1
    else:
        left = mid + 1

print(left)