# https://www.acmicpc.net/problem/11444

N = int(input())

MOD = 1_000_000_007

def matmul(A, B):
    result = [[0, 0], [0, 0]]    
    for i in range(2):
        for k in range(2):
            aik = A[i][k]
            for j in range(2):
                result[i][j] = (result[i][j] + aik * B[k][j]) % MOD
    return result

result = [[1, 0], [0, 1]]
A = [[0, 1], [1, 1]]
while N:
    if N & 1:
        result = matmul(result, A)
    N >>= 1
    A = matmul(A, A)

print(result[0][1])