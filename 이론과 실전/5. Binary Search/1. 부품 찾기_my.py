import sys

n = int(input())
item_list = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
find_list = list(map(int, sys.stdin.readline().rstrip().split()))

item_list.sort()

def binary_search(start, end, to_find):
    mid = int((end+start)/2)
    if start > end:
        return False
    if to_find == item_list[mid]:
        return True
    elif to_find > item_list[mid]:
        return binary_search(mid+1, end, to_find)
    else:
        return binary_search(start, mid-1, to_find)

result = []
for num in find_list:
    if binary_search(0, n-1, num) == True:
        result.append("yes")
    else:
        result.append("no")

print(*result)