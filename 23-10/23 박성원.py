# https://www.acmicpc.net/problem/1086

import sys

inp = sys.stdin.readline

def resolve(bitmask):
    for i in range(N):
        if bitmask & (1 << i) == 0:
            continue
        order = orders[i]
        complement = bitmask & ~(1 << i)
        num = nums[i] % K
        for j in range(K):
            dp[bitmask][(j * order + num) % K] += dp[complement][j]

N = int(inp())
nums = [int(inp()) for _ in range(N)]
K = int(inp())
orders = [10**len(str(num)) % K for num in nums]

dp = [[0] * K for _ in range(2**N)]
dp[0][0] = 1

for i in range(2**N):
    resolve(i)

numerator = dp[-1][0]
denominator = sum(dp[-1])
factor_primes = [2, 3, 5, 7, 11, 13]

for p in factor_primes:
    while numerator % p == 0 and denominator % p == 0:
        numerator //= p
        denominator //= p

print(numerator, "/", denominator, sep="")