loca = input()

row = int(loca[1])
col = ord(loca[0]) - ord("a") + 1 # "a" -> 1

cur = [row, col]

ways = [
    [row-1, col-2],
    [row-1, col+2],
    [row+1, col-2],
    [row+1, col+2],
    [row-2, col-1],
    [row-2, col+1],
    [row+2, col-1],
    [row+2, col+1],
]

result = 8

for way in ways:
    if way[0] <= 0 or way[0] >= 9 or way[1] <= 0 or way[1] >= 9:
        result -= 1

print(result)