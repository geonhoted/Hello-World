N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]

from itertools import combinations

for each_i in combinations(numbers, M):
    for m in each_i:
        print(m, end = " ")
