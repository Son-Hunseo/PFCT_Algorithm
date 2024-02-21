import sys

n = int(input())
storage = list(map(int, sys.stdin.readline().rstrip().split()))

result = [0] * 101
result[1] = storage[0]

for i in range(2, len(storage)+1):
    result[i] = max(result[i-1], result[i-2]+storage[i-1])

print(result[n])