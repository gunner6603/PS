# https://www.acmicpc.net/problem/18185

import sys

inp = sys.stdin.readline

N = int(inp())
nums = list(map(int, inp().split()))
cost = 0

for i in range(N - 2):
    if nums[i + 1] > nums[i + 2]:
        diff = min(nums[i], nums[i + 1] - nums[i + 2])
        cost += 5 * diff
        nums[i] -= diff
        nums[i + 1] -= diff
    min_idx = min(range(3), key=lambda j: nums[i + j])
    if min_idx == 0:
        cost += 7 * nums[i]
        nums[i + 1] -= nums[i]
        nums[i + 2] -= nums[i]
        nums[i] = 0
    elif min_idx == 1:
        cost += 3 * nums[i] + 4 * nums[i + 1]
        nums[i + 2] -= nums[i + 1]
        nums[i] = 0
        nums[i + 1] = 0
    else:
        min_val, max_val = min(nums[i], nums[i + 1]), max(nums[i], nums[i + 1])
        cost += 3 * max_val + 2 * min_val + 2 * nums[i + 2]
        nums[i] = 0
        nums[i + 1] = 0
        nums[i + 2] = 0

min_val, max_val = min(nums[-2], nums[-1]), max(nums[-2], nums[-1])
cost += 2 * min_val + 3 * max_val

print(cost)