# https://www.acmicpc.net/problem/17401

import sys

inp = sys.stdin.readline

DIV = 1_000_000_007
T, N, D = map(int, inp().split())
I = [[1 if j == i else 0 for j in range(N)] for i in range(N)]

vm = [I] # vessel map
for _ in range(T):
    link = [[0] * N for _ in range(N)]
    M = int(inp())
    for _ in range(M):
        a, b, c = map(int, inp().split())
        link[a - 1][b - 1] = c
    vm.append(link)

def mul(A, B):
    C = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for k in range(N):
            aik = A[i][k]
            for j in range(N):
                C[i][j] = (C[i][j] + aik * B[k][j]) % DIV
    
    return C

for i in range(T):
    vm[i + 1] = mul(vm[i], vm[i + 1])

def exp(A, k):
    result = I
    
    while k:
        if k & 1:
            result = mul(result, A)
        k >>= 1
        A = mul(A, A)
    
    return result

answer = mul(exp(vm[T], D // T), vm[D % T])
for row in answer:
    print(*row)