# https://www.acmicpc.net/problem/19585

import sys
from collections import defaultdict

inp = sys.stdin.readline

C, N = map(int, inp().split())

class TrieNode:
    def __init__(self):
        self.data = False
        self.next = defaultdict(TrieNode)

color_root = TrieNode()
for _ in range(C):
    color = inp().rstrip()
    cur_node = color_root
    for char in color:
        cur_node = cur_node.next[char]
    cur_node.data = True

nickname = {inp().rstrip() for _ in range(N)}
    
def check(team_name):
    cur_node = color_root
    for i, char in enumerate(team_name):
        if char not in cur_node.next:
            break
        cur_node = cur_node.next[char]
        if cur_node.data and team_name[i + 1:] in nickname:
            return True
            
    return False

Q = int(inp())
for _ in range(Q):
    team_name = inp().rstrip()
    if check(team_name):
        print("Yes")
    else:
        print("No")