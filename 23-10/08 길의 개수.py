# https://www.acmicpc.net/problem/1533

import sys

inp = sys.stdin.readline

MOD = 1_000_003
N, S, E, T = map(int, inp().split())

graph = [list(map(int, inp().rstrip())) for _ in range(N)]

new_N = N
for row in graph:
    row_max = max(row)
    if row_max > 1:
        new_N += (row_max - 1)

new_graph = [[0] * new_N for _ in range(new_N)]
cur_new_vertex = N
for i in range(N):
    row = graph[i]
    row_max = max(row)
    for k in range(row_max - 2):
        new_graph[cur_new_vertex + k][cur_new_vertex + k + 1] = 1
    for j, elem in enumerate(row):
        if elem == 1:
            new_graph[i][j] = 1
        elif elem >= 2:
            new_graph[i][cur_new_vertex] = 1
            new_graph[cur_new_vertex + elem - 2][j] = 1
    if row_max > 1:
        cur_new_vertex += row_max - 1

def matmul(A, B): # for square matrices A and B
    result = [[0] * new_N for _ in range(new_N)]
    for i in range(new_N):
        for k in range(new_N):
            A_ik = A[i][k]
            for j in range(new_N):
                result[i][j] = (result[i][j] + A_ik * B[k][j]) % MOD
    return result

def matexp(A, k):
    result = [[1 if i == j else 0 for i in range(new_N)] for j in range(new_N)] # identity matrix
    while k:
        if k & 1:
            result = matmul(result, A)
        k >>= 1
        A = matmul(A, A)
    return result

print(matexp(new_graph, T)[S - 1][E - 1])