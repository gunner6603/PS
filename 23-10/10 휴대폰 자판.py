# https://www.acmicpc.net/problem/5670

import sys
from collections import defaultdict

inp = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.data = False
        self.next = defaultdict(TrieNode)

def insert(root, word):
    cur_node = root
    for char in word:
        cur_node = cur_node.next[char]
    cur_node.data = True

def count(root, word):
    cur_node = root.next[word[0]]
    cnt = 1
    for char in word[1:]:
        if cur_node.data + len(cur_node.next) > 1:
            cnt += 1
        cur_node = cur_node.next[char]
        
    return cnt
    
def solution():
    N = int(inp())
    words = [inp().rstrip() for _ in range(N)]
    root = TrieNode()
    
    for word in words:
        insert(root, word)
        
    cnt = 0
    for word in words:
        cnt += count(root, word)

    return round(cnt / N, 2)

while True:
    try:
       print("{:.2f}".format(solution()))
    except:
        break