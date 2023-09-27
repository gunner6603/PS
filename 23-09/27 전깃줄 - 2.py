import sys
from bisect import bisect_left

inp = sys.stdin.readline

N = int(inp())
lines = [tuple(map(int, inp().split())) for _ in range(N)]
seq = [line[0] for line in sorted(lines, key=lambda x: x[1])]

dp1 = []
dp2 = [0]

for num in seq:
    idx = bisect_left(dp2, num)
    if idx == len(dp2):
        dp2.append(num)
    else:
        dp2[idx] = num
    dp1.append(idx)

cur = len(dp2) - 1
stack = []

for i in range(len(dp1) - 1, -1, -1):
    if dp1[i] == cur and (not stack or stack[-1] > seq[i]):
        cur -= 1
        stack.append(seq[i])
        if cur == 0:
            break

print(len(seq) - len(stack))

stack_idx = len(stack) - 1
removal = []
for num in seq:
    if num == stack[stack_idx]:
        stack_idx -= 1
    else:
        removal.append(num)

removal.sort()
for r in removal:
    print(r)