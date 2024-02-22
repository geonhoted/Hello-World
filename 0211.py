#1010

sticks = [64, 32, 16, 8, 4, 2, 1]

l = int(input())

n = 0


for i in range(7):
    if l == 0:
        break
    elif sticks[i] <= l:
        l = l - sticks[i]
        n += 1

print(n)