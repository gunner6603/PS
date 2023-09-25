# https://www.acmicpc.net/problem/27172

import sys

inp = sys.stdin.readline

N = int(inp())
nums = list(map(int, inp().split()))

max_val = max(nums)
score = [None] * (max_val + 1)

for num in nums:
    score[num] = 0

for num in nums:
    cnt = 0
    for mul in range(2 * num, max_val + 1, num):
        if score[mul] is not None:
            score[mul] -= 1
            cnt += 1
    score[num] += cnt

for num in nums:
    print(score[num], end=" ")