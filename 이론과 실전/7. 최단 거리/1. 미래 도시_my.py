n, m = map(int, input().split())

# 초기 설정
table = [[99999999 for _ in range(n+1)] for _ in range(n+1)]

# 연결된 노드 거리 1로 초기화
for i in range(m):
    start, end = map(int, input().split())
    table[start][end] = 1
    table[end][start] = 1

# 자기 자신과의 연결 0으로 초기화
for i in range(n):
    table[i+1][i+1] = 0

x, k = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            table[i][j] = min(table[i][j], table[i][k]+table[k][j])

if table[1][x] and table[x][k] <= m:
    print(table[1][k] + table[k][x])
else:
    print(-1)
