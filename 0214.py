def makeone(x, memo):
    if x in memo:  # 이미 계산된 값인지 확인
        return memo[x]
    if x == 1:
        return 0  # 1이면 연산이 필요 없으므로 0 반환

    # 1로 만들기 위한 최소 연산 횟수 계산
    count = makeone(x-1, memo) + 1  # -1 연산

    if x % 2 == 0:
        count = min(count, makeone(x//2, memo) + 1)  # //2 연산
    if x % 3 == 0:
        count = min(count, makeone(x//3, memo) + 1)  # //3 연산

    memo[x] = count  # 계산된 값을 메모에 저장
    return count

x = int(input())  # 사용자 입력 받기
memo = {}  # 메모이제이션을 위한 딕셔너리
print(makeone(x, memo))  # 최소 연산 횟수 출력
