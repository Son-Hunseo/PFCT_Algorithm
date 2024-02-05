n, m = map(int, input().split())
array = []
for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)

candi = []
for i in range(n):
    candi.append(min(array[i]))
print(max(candi))