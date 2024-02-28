import sys
input = sys.stdin.readline

computers = int(input())
n = int(input())
network = [list(map(int, input().split())) for _ in range(n)]

virus = [1]

def checkvirus(network, k):
    global virus
    for i in range(n):
        if k in network[i]:
            for j in range(2):
                if network[i][j] != k and network[i][j] not in virus:
                    virus.append(network[i][j])
                    checkvirus(network, network[i][j])

checkvirus(network, 1)
print(len(virus)-1)