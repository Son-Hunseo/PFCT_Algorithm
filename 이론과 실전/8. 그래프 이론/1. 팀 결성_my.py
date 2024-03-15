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
    # 내가 틀렸던 부분
    # 미리 함수 값을 변수에 저장 시키는게 시간적으로 효율적
    a = find_parent(num1)
    b = find_parent(num2)
    # 여기서 내가 틀렸던 부분을 주석으로 달면 아래와 같은데
    # 이게 틀린 이유는 이렇게하면 부모를 묶는게 아니라 직접적인 노드끼리의 연결이다.
    if a < b:
        # parent[num2] = num1
        parent[b] = a
    else:
        # parent[num1] = num2
        parent[a] = b

for _ in range(m):
    method, a, b = map(int, sys.stdin.readline().rstrip().split())
    if method == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')