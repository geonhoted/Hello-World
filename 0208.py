import math

c, a, b = map(int, input().split())

k = c/((a**2+b**2)**(1/2))

print(f"{math.floor(a*k)} {math.floor(b*k)}")