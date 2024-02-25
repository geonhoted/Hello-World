def makeone(x):
    dp = [0] * (x + 1)  # 연산 횟수를 저장할 리스트, 인덱스 0에서 x까지

    for i in range(2, x + 1):  # 1은 연산이 필요 없으므로 2부터 시작
        # 현재 숫자에서 1을 빼는 경우
        dp[i] = dp[i - 1] + 1

        # 현재 숫자가 2로 나누어 떨어지는 경우, 더 적은 연산 횟수를 선택
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 현재 숫자가 3으로 나누어 떨어지는 경우, 더 적은 연산 횟수를 선택
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[x]  # x를 1로 만드는 최소 연산 횟수 반환

x = int(input())
print(makeone(x))
