# 백준 2294와 같은 문제
n, m = map(int, input().split())

money = []
for i in range(n):
    value = int(input())
    money.append(value)

money = list(set(money))
min_money = min(money)

# 백준 2294의 경우 아래와 같이 dp테이블 설정
# dp_table = [0] * 100001
dp_table = [0] * 10001

for i in range(min(money), m+1):
    if i in money:
        dp_table[i] = 1
    else:
        candi = []
        for value in money:
            if (i-value >= min_money) & (dp_table[i-value] != 0):
                candi.append(dp_table[i-value])
        if candi:
                dp_table[i] = min(candi) + 1

for i in range(len(dp_table)):
    if dp_table[i] == 0:
        dp_table[i] = -1

print(dp_table[m])