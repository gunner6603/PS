import sys
from bisect import bisect_left

inp = sys.stdin.readline

N = int(inp())
nums = list(map(int, inp().split()))

dp = []

for num in nums:
    idx = bisect_left(dp, num)
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

print(len(dp))