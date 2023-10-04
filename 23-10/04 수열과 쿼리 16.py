# https://www.acmicpc.net/problem/14428

import sys
import math

inp = sys.stdin.readline

N = int(inp())
seq = [0] + list(map(int, inp().split()))
seq.append(float('inf'))

M = int(inp())
query = [tuple(map(int, inp().split())) for _ in range(M)]

tree_height = math.ceil(math.log2(N))
tree = [-1] * 2**(tree_height + 1) # 해당 구간의 최소 인덱스 저장

def make_tree(tree_node, seq_left, seq_right):
    if seq_left == seq_right:
        tree[tree_node] = seq_left
        return seq_left
    
    mid = seq_left + (seq_right - seq_left) // 2
    left_val = make_tree(tree_node*2, seq_left, mid)
    right_val = make_tree(tree_node*2 + 1, mid + 1, seq_right)
    val = min(left_val, right_val, key=lambda i: seq[i])
    tree[tree_node] = val
    return val

def update_tree(tree_node, seq_left, seq_right, seq_update): # seq 업데이트 후 호출
    if not (seq_left <= seq_update <= seq_right):
        return tree[tree_node]
    if seq_left == seq_right:
        return tree[tree_node]
    mid = seq_left + (seq_right - seq_left) // 2
    left_val = update_tree(tree_node*2, seq_left, mid, seq_update)
    right_val = update_tree(tree_node*2 + 1, mid + 1, seq_right, seq_update)
    val = min(left_val, right_val, key=lambda i: seq[i])
    tree[tree_node] = val
    return val
            
def search_tree(tree_node, seq_left, seq_right, search_left, search_right):
    if search_right < seq_left or seq_right < search_left:
        return -1
    if search_left <= seq_left and seq_right <= search_right:
        return tree[tree_node]
    mid = seq_left + (seq_right - seq_left) // 2
    left_val = search_tree(tree_node*2, seq_left, mid, search_left, search_right)
    right_val = search_tree(tree_node*2 + 1, mid + 1, seq_right, search_left, search_right)
    return min(left_val, right_val, key=lambda i: seq[i])

make_tree(1, 1, N)

for t, i, j in query:
    if t == 1:
        seq[i] = j
        update_tree(1, 1, N, i)
    elif t == 2:
        print(search_tree(1, 1, N, i, j))