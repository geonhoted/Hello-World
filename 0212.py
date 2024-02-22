w = int(input())

if w % 5 == 0:
    print(w // 5)

else:
    bag5 = w // 5  
    for i in range(bag5, -1, -1):  
        remainder = w - (i * 5)  
        if remainder % 3 == 0:  
            print(i + (remainder // 3))
            break
    else:
        print(-1) 
