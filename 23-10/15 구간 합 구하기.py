# https://www.acmicpc.net/problem/2042

import sys, math

inp = sys.stdin.readline

N, M, K = map(int, inp().split())

nums = [-1] + [int(inp()) for i in range(N)]
tree = [-1] * 2**(math.ceil(math.log2(N)) + 1)

def make_tree(tree_idx, num_left, num_right):
    if num_left == num_right:
        tree[tree_idx] = nums[num_left]
        return tree[tree_idx]
    mid = (num_left + num_right) // 2
    tree[tree_idx] = make_tree(tree_idx*2, num_left, mid) + make_tree(tree_idx*2 + 1, mid + 1, num_right)
    return tree[tree_idx]

def change(tree_idx, num_left, num_right, change_idx, change_num):
    if not (num_left <= change_idx <= num_right):
        return tree[tree_idx]
    if num_left == num_right:
        tree[tree_idx] = change_num
        return change_num
    mid = (num_left + num_right) // 2
    tree[tree_idx] = change(tree_idx*2, num_left, mid, change_idx, change_num) + change(tree_idx*2 + 1, mid + 1, num_right, change_idx, change_num)
    return tree[tree_idx]
    
    
def cal_sum(tree_idx, num_left, num_right, lower_bound, upper_bound):
    if lower_bound <= num_left and num_right <= upper_bound:
        return tree[tree_idx]
    if num_right < lower_bound or upper_bound < num_left:
        return 0
    mid = (num_left + num_right) // 2
    return cal_sum(tree_idx*2, num_left, mid, lower_bound, upper_bound) + cal_sum(tree_idx*2 + 1, mid + 1, num_right, lower_bound, upper_bound)

make_tree(1, 1, N)
for _ in range(M + K):
    a, b, c = map(int, inp().split())
    if a == 1:
        change(1, 1, N, b, c)
    elif a == 2:
        result = cal_sum(1, 1, N, b, c)
        print(result)