import sys

inp = sys.stdin.readline

seq = inp().rstrip()

def find_pal_len_odd(i):
    left, right = i, i
    while left - 1 >= 0 and right + 1 < len(seq) and seq[left - 1] == seq[right + 1]:
        left -= 1
        right += 1
    return right - left + 1

def find_pal_len_even(i, j):
    left, right = i, j
    while left - 1 >= 0 and right + 1 < len(seq) and seq[left - 1] == seq[right + 1]:
        left -= 1
        right += 1
    return right - left + 1

pal_len = [0] * (2*len(seq) - 1)
for i in range(len(seq)):
    pal_len[2*i] = find_pal_len_odd(i)

for i in range(len(seq) - 1):
    pal_len[2*i + 1] = find_pal_len_even(i + 1, i)
    
dp = []
for i in range(len(seq)):
    min_val = float('inf')
    for j in range(0, i + 1):
        # j ~ i 팰린드롬 체크
        if pal_len[j + i] >= i - j + 1:
            if j == 0:
                min_val = 1
                break
            min_val = min(min_val, dp[j - 1] + 1)
    dp.append(min_val)

print(dp[-1])