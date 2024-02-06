max_row, max_col = map(int, input().split())
cur_x, cur_y, cur_dir = map(int, input().split())
game_map = []
for _ in range(max_row):
    row = list(map(int, input().split()))
    game_map.append(row)

direction = [0, 3, 2, 1]
dx = [-1, 0, +1, 0]
dy = [0, -1, 0, +1]

count = 1
change = 0

def change_dir(cur_dir):
    cur_dir_index = direction.index(cur_dir)
    if cur_dir_index == 3:
        after_dir = 0
    else:
        after_dir = direction[cur_dir_index+1]
    return after_dir

while True:
    # 현재 있는 칸 방문 처리
    game_map[cur_x][cur_y] = 2
    # 4방향을 모두 확인 했다면
    if change == 4:
        change = 0
        # 뒤가 이미 가본 칸이려면
        if game_map[cur_x-dx[cur_dir_index]][cur_y-dy[cur_dir_index]] == 2:
            # 뒤로 이동
            cur_x = cur_x-dx[cur_dir_index]
            cur_y = cur_y-dy[cur_dir_index]
        # 뒤가 바다라면
        else:
            break
    else:
        # 방향 전환
        cur_dir = change_dir(cur_dir)
        cur_dir_index = direction.index(cur_dir)
        change += 1
        # 해당 방향으로 갈 수 있다면
        if game_map[cur_x+dx[cur_dir_index]][cur_y+dy[cur_dir_index]] == 0:
            change = 0
            count += 1
            cur_x = cur_x+dx[cur_dir_index]
            cur_y = cur_y+dy[cur_dir_index]
        # 갈 수 없다면
        else:
            continue

print(count)