# https://www.acmicpc.net/problem/15678

import sys
from heapq import heappush, heappop

inp = sys.stdin.readline

N, D = map(int, inp().split())
K = list(map(int, inp().split()))
heap = []

for i in range(N):
    while heap and heap[0][1] + D < i:
        heappop(heap)
    if heap:
        K[i] -= heap[0][0]
    if K[i] > 0:
        heappush(heap, (-K[i], i))

print(max(K))