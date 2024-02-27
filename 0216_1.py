def island(position, w, h):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    def dfs(x, y):
        if x < 0 or x >= h or y < 0 or y >= w or position[x][y] != 1:
            return
        position[x][y] = 2
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    island_count = 0
    for i in range(h):
        for j in range(w):
            if position[i][j] == 1:
                dfs(i, j)
                island_count += 1
    return island_count

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    position = []
    for i in range(h):
        position.append(list(map(int, input().split())))
    print(island(position, w, h))
