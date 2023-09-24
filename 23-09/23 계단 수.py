N = int(input())
DIV = 1_000_000_000

dp = [[0] * 2**10 for _ in range(10)]

for i in range(1, 10):
    dp[i][1 << i] = 1

for _ in range(N - 1):
    dp_prev = dp
    dp = [[0] * 2**10 for _ in range(10)]
    for i in range(10):
        for j in range(2**10):
            val = dp_prev[i][j]
            for k in [i - 1, i + 1]:
                if 0 <= k < 10:
                    dp[k][j | 1 << k] += val

print(sum(row[-1] for row in dp) % DIV)