#1000
#a, b = map(int, input().split())
#print(a+b)


#2338
#a = int(input())
#b = int(input())

#print(a+b)
#print(a-b)
#print(a*b)

#3003
n = input().split()
n = [int(x) for x in n]

o = [1, 1, 2, 2, 2, 8]
result = []

for i in range(6):
    value = o[i] - n[i]
    result.append(str(value))
    
print(' '.join(result))