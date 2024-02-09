n = int(input())
last = n*2 - 1

for i in range(n):
    star = '*'*(i*2+1)
    print(star.rjust(n+i))