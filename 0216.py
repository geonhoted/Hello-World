N, M, V = map(int, input().split())
connections = [list(map(int, input().split())) for _ in range(M)]
lines = [[0] * N for _ in range(N)]

# 연결 정보를 기반으로 lines 리스트 갱신
for connection in connections:
    from_node, to_node = connection
    lines[from_node - 1][to_node - 1] = 1
    lines[to_node - 1][from_node - 1] = 1  # 무방향 그래프이므로 양쪽 모두 연결되어 있음을 표시

def DFS(S, line):
    visited = [False] * N  # 방문 여부를 저장하는 리스트
    result = []  # DFS를 수행한 결과로서, 방문한 노드들의 순서를 저장하는 리스트
    _DFS(S, line, visited, result)  # 실제 DFS 실행
    return result

def _DFS(S, line, visited, result):
    result.append(S)  # 현재 노드를 결과 리스트에 추가
    visited[S - 1] = True  # 현재 노드를 방문했음을 표시

    # 현재 노드와 연결된 노드를 탐색
    for i in range(N):
        if line[S - 1][i] == 1 and not visited[i]:
            _DFS(i + 1, line, visited, result)  # 재귀적으로 연결된 노드를 탐색

def BFS(S, line):
    visited = [False] * N  # 방문 여부를 저장하는 리스트
    queue = [S]  # 큐를 생성하고 시작 노드를 넣음
    visited[S - 1] = True  # 시작 노드를 방문했음을 표시
    result = []  # BFS를 수행한 결과로서, 방문한 노드들의 순서를 저장하는 리스트

    while queue:
        node = queue.pop(0)  # 큐에서 하나의 노드를 꺼냄
        result.append(node)  # 방문한 노드를 결과 리스트에 추가

        # 현재 노드와 연결된 노드를 탐색
        for i in range(N):
            if line[node - 1][i] == 1 and not visited[i]:
                queue.append(i + 1)
                visited[i] = True

    return result

print(' '.join(map(str, DFS(V, lines))))
print(' '.join(map(str, BFS(V, lines))))

