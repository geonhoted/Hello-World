#11650

points = []
n = int(input())
for i in range(n):
    points.append(list(map(int, input().split())))

sorted_points = sorted(points, key = lambda x : (x[0], x[1]))

for i in range(n):
    print(sorted_points[i][0], sorted_points[i][1])