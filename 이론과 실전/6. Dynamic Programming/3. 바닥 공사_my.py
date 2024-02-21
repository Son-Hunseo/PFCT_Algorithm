# 백준 11727과 같은 문제
n = int(input())

result = [0]*1001
result[1] = 1

for i in range(2, 1001):
    if i%2 == 0:
        result[i] = 2*result[i-1] + 1
    else:
        result[i] = 2*result[i-1] - 1

print(result[n]%796796)