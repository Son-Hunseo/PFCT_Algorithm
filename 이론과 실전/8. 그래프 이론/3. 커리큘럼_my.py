# 위상정렬만 수행하고 문제를 못풀었다. -> 이후 고쳤다.
# 주의! : list의 경우 변수만 할당할 경우 인스턴스를 할당하게 되므로 time을 result로 복사할 때 deepcopy()를 사용하여야한다.
# 한 단계씩 진행하면서 현재 큐에서 꺼낸 노드와 연결된 노드의 걸리는 시간을 max(대상 노드의 result시간, 현재 노드의 result시간 + 대상 노드의 time시간) 이렇게 갱신해주었다.

from collections import deque
import copy

n = int(input())
time_cost = [0]
table = [[] for i in range(n+1)]

for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] != -1:
            if j == 0:
                time_cost.append(data[j])
            else:
                table[i].append(data[j])

# 의미없는 노드의 길이를 0이 아닌 길이로 맞추기 위함
table[0].append(99999999)
q = deque()

for i in range(len(table)):
    if len(table[i]) == 0:
        q.append(i)

result = copy.deepcopy(time_cost)
order = []

while q:
    now = q.popleft()
    order.append(now)
    for i in range(len(table)):
        if now in table[i]:
            table[i].remove(now)
    for i in range(len(table)):
        if (len(table[i]) == 0) and (i not in order) and (i not in q):
            q.append(i)
            # 이 부분을 생각하지 못했었다.
            result[i] = max(result[i], result[now]+time_cost[i])

for i in range(1, len(result)):
    print(result[i])