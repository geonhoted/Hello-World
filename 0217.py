def island(position, w, h):
    n = 0
    check = [[False]*w for i in range(h)]

    for i in range(w):
        for j in range(h):
            if position[i][j] == 1:
                if (position[i-1][j-1] == 1 
                    or position[i-1][j] == 1 
                    or position[i-1][j+1] == 1 
                    or position[i][j-1] == 1 
                    or position[i][j+1] == 1 
                    or position[i+1][j-1] == 1 
                    or position[i+1][j] == 1 
                    or position[i+1][j+1] == 1):
                    check[i][j] = True
    return(sum(row.count(True) for row in check)


while(True):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    position = []
    for i in range(h):
        position.append(list(map(int, input().split())))
    print(island(position, w, h))


def island(position, w, h):
    n = 0
    check = [[False]*w for i in range(h)]

    for i in range(w):
        for j in range(h):
            if position[i][j] >= 1:
                if position[i][j+1] == 1:
                    position[i][j+1] = 2
                if position[i+1][j] == 1:
                    position[i+1][j] = 2
                if position[i+1][j+1] == 1:
                    position[i+1][j+1] = 2
                    check[i][j] = True
    return(sum(row.count(1) for row in position)

    
