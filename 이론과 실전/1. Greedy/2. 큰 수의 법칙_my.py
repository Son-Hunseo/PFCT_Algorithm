import sys

n, m, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

index1 = -99999
index2 = -99999
num1 = -99999
num2 = -99999

for i in range(n):
    if array[i] > num1:
        index1 = i
        num1 = array[i]

array.pop(index1)

for i in range(n-1):
    if array[i] > num2:
        index2 = i
        num2 = array[i]

cal1 = m//(k+1)
cal2 = m%(k+1)

result = ((num1*k) + num2)*cal1 + (num1*cal2)
print(result)