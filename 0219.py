import sys
input = sys.stdin.readline

n = int(input())
score = [0]
for _ in range(n):
    score.append(int(input()))

result = 0
list = []
checkplusone = 0

def plusone(score, i):
    global result
    global list
    global checkplusone
    if checkplusone == 3:
        return
    result = result + score[i+1]
    checkplusone += 1
    if i+1 == n:
        list.append(result)
        return 0
    elif i+2 == n:
        plusone(score, i+1)
    elif i+2 < n:
        plusone(score, i+1)
        plustwo(score, i+1)


def plustwo(score, i):
    global result
    global list
    global checkplusone
    result = result + score[i+2]
    checkplusone = 0
    if i+2 == n:
        list.append(result)
        return 0
    elif i+3 == n:
        plusone(score, i+1)
    elif i+3 < n:
        plusone(score, i+1)
        plustwo(score, i+1)

plusone(score, 0)
plustwo(score, 0)

print(max(list))
    