# https://www.acmicpc.net/problem/1725

import sys

inp = sys.stdin.readline

def cal_max_area(start, end):
    if start == end:
        return nums[start]
    
    mid = (start + end) // 2
    area = nums[mid]
    height = nums[mid]
    left = mid
    right = mid
    
    while left > start and right < end:
        if nums[left - 1] < nums[right + 1]:
            right += 1
            height = min(height, nums[right])
        else:
            left -= 1
            height = min(height, nums[left])
        area = max(area, (right - left + 1) * height)
        
    while right < end:
        right += 1
        height = min(height, nums[right])
        area = max(area, (right - left + 1) * height)
        
    while left > start:
        left -= 1
        height = min(height, nums[left])
        area = max(area, (right - left + 1) * height)    
    
    return max(cal_max_area(start, mid), cal_max_area(mid + 1, end), area)

N = int(inp())
nums = [int(inp()) for _ in range(N)]
print(cal_max_area(0, N - 1))