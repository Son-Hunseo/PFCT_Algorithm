n = int(input())
way = list(map(str, input().split()))

start = [1, 1]

for i in range(len(way)):
    if way[i] == "L":
        if start[1] <= 1:
            continue
        else:
            start[1] -= 1
    elif way[i] == "R":
        if start[1] >= n:
            continue
        else:
            start[1] += 1
    elif way[i] == "U":
        if start[0] <= 1:
            continue
        else:
            start[0] -= 1
    elif way[i] == "D":
        if start[0] >= n:
            continue
        else:
            start[0] += 1

print(*start)