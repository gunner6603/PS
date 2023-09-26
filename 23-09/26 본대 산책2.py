D = int(input())
N = 8
DIV = 1_000_000_007
link = [
    [1, 3],
    [0, 2, 3],
    [1, 3, 4, 5],
    [0, 1, 2, 5],
    [2, 5, 6],
    [2, 3, 4, 7],
    [4, 7],
    [5, 6]    
]

k = 0
while (D >> k) > 0:
    k += 1

dp = [[[0] * N for __ in range(N)] for _ in range(k)]

for u in range(N):
    for v in link[u]:
        dp[0][u][v] = 1
        dp[0][v][u] = 1
        
for i in range(1, k):
    for u in range(N):
        for v in range(N):
            for b in range(N):
                dp[i][u][v] = (dp[i][u][v] + dp[i - 1][u][b] * dp[i - 1][b][v]) % DIV
            
ones = []
for i in range(k):
    if D & (1 << i) > 0:
        ones.append(i)

result = [[1 if j == i else 0 for j in range(N)] for i in range(N)]
for i in range(len(ones)):
    cur = dp[ones[i]]
    new_result = [[0] * N for _ in range(N)]
    for u in range(N):
        for v in range(N):
            for b in range(N):
                new_result[u][v] = (new_result[u][v] + result[u][b] * cur[b][v]) % DIV
    result = new_result
    
print(result[0][0])