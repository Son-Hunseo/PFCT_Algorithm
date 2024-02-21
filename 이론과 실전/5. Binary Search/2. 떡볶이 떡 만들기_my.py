# 백준 2805 나무자르기 문제와 동일한 문제이다.

import sys

n, m = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

result = []
def BS(start, end, target):
    # 종료 조건
    if start > end:
        return None
    mid = (end+start)//2
    length = []

    for i in range(len(data)):
        if data[i] >= mid:
            length.append(data[i]-mid)
        else:
            length.append(0)

    if sum(length) >= target:
        result.append(mid)
        BS(mid+1, end, target)
        return True
    else:
        BS(start, mid-1, target)
        return False

BS(0, max(data), m)
print(max(result))
