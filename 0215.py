n = int(input())
costs = []

for i in range(n):
    costs.append(list(map(int, input().split())))  # 입력값을 정수로 변환하여 저장

def min_cost(costs):
    dp = [[0]*3 for _ in range(n)]

    # 초기값 설정
    dp[0] = costs[0]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    # 마지막 칸에서 각 색깔로 칠하는 비용 중 최소값 반환
    return min(dp[-1])

print(min_cost(costs))


