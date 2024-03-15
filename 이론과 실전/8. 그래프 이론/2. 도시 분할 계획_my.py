import sys

n, m = map(int, input().split())

parent = []
for i in range(n+1):
    parent.append(i)


def find_parent(num):
    if parent[num] != num:
        parent[num] = find_parent(parent[num])
    return parent[num]

def union_parent(num1, num2):
    a = find_parent(num1)
    b = find_parent(num2)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

candi = []

for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    candi.append((cost, a, b))

candi.sort()
result = []

for i in range(len(candi)):
    a = candi[i][1]
    b = candi[i][2]
    cost = candi[i][0]

    # 이 부분을 틀렸었다. 이 부분 구현 기억하기!!
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result.append(cost)

result.pop()
print(sum(result))

