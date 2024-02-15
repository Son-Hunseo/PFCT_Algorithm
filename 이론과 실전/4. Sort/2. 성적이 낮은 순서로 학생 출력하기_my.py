n = int(input())

array = []
for _ in range(n):
    data = list(map(str, input().split()))
    data[1] = int(data[1])
    array.append(data)

def num_ord(data):
    return data[1]

result = sorted(array, key=num_ord)

for data in result:
    print(data[0], end=" ")