n = int(input())

x = []
y = []

for i in range(n):
    a,b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(n):
    print(x[i]+y[i])