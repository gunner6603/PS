# https://www.acmicpc.net/problem/17387

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def resolve_relative_pos(x1, y1, x2, y2, a, b):
    if x1 == x2:
        if a == x1:
            return 0
        elif a < x1:
            return 1
        else:
            return 2
    elif y1 == y2:
        if b == y1:
            return 0
        elif b < y1:
            return 1
        else:
            return 2
    else:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        val = (x2 - x1) * (b - y1) - (y2 - y1) * (a - x1)    
        if val == 0:
            return 0
        elif val < 0:
            return 1
        else:
            return 2

a = resolve_relative_pos(x1, y1, x2, y2, x3, y3)
b = resolve_relative_pos(x1, y1, x2, y2, x4, y4)
c = resolve_relative_pos(x3, y3, x4, y4, x1, y1)
d = resolve_relative_pos(x3, y3, x4, y4, x2, y2)

answer = 1

if a == b and a != 0:
    answer = 0
elif c == d and c != 0:
    answer = 0
if a == b == 0:
    points = [(x1, y1, 0), (x2, y2, 0), (x3, y3, 1), (x4, y4, 1)]
    points.sort()
    if points[0][2] == points[1][2] and points[1][:2] != points[2][:2]:
        answer = 0

print(answer)