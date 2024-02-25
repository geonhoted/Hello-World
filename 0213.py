cases = int(input())

for i in range(cases):
    x, y, n = map(int, input().split())

    pos = []
    count = n

    for i in range(n):
        pos.append(input().split())

    for i in range(n):
        for j in range(i+1, len(pos)):
            if abs(int(pos[i][0]) - int(pos[j][0])) + abs(int(pos[i][1]) - int(pos[j][1])) == 1:
                count = count - 1
                break

    print(count)

            