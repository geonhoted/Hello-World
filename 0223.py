n = int(input())

count = 99

if n < 100:
    print(n)
else:
    for i in range(100, n+1):
        a = i // 100  
        b = (i // 10) % 10  
        c = i % 10  
        if (a-b) == (b-c):
            count += 1
    print(count)
