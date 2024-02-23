import sys
import heapq

n, m, c = map(int, input().split())

data = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    data[x].append((z, y))

result = [99999999 for _ in range(n+1)]
result[c] = 0

check = [0 for _ in range(n+1)]
q = []

heapq.heappush(q, (0, c))

while q:
    cur = heapq.heappop(q)
    if check[1] == 0:
        check[cur[1]] = 1
        for con in data[cur[1]]:
            if result[con[1]] > (result[cur[1]]+con[0]):
                result[con[1]] = result[cur[1]]+con[0]
                heapq.heappush(q, con)
    else:
        continue

city_num = 0
city_max = 0
for i in range(1, len(result)):
    if 0 < result[i] <= m:
        city_num += 1
        if result[i] > city_max:
            city_max = result[i]

print(city_num, str(city_max))