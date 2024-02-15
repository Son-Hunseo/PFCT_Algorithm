# 시간 너무 오래 걸리는 듯
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

list = [0 for _ in range(10000001)]

A.sort()

for num in A:
    list[num] += 1

for num in B:
    list[num] += 1

Big = []

cnt = 0
for i in range(10000000, 0, -1):
    if cnt == k:
        break
    if list[i] != 0:
        for j in range(list[i]):
            if cnt == k:
                break
            Big.append(i)
            cnt += 1
    else:
        continue

result = sum(Big)
result = result + sum(A[k:])

print(result)
