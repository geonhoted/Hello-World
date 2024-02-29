from itertools import permutations

N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]

for each_i in permutations(numbers, M):
    tuple = each_i
    for m in tuple:
        print(m, end = " ")