# https://www.acmicpc.net/problem/1328

N, L, R = map(int, input().split())
MOD = 1_000_000_007
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][1] = 1

for k in range(1, N):
    for i in range(k + 1, 0, -1):
        for j in range(k + 2 - i, 0, -1):
            dp[i][j] = (dp[i][j] * (k - 1) + dp[i - 1][j] + dp[i][j - 1]) % MOD
            
print(dp[L][R])