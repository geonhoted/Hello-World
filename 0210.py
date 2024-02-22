n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    result = 1
    for j in range(b-a):
        result = result * (b-j) / (j+1)
    
    print(int(result))