n = int(input())
list = input().split()
v = input()

num = 0

for i in range(len(list)):
    if v == list[i]:
        num += 1

print(num)
