def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node):
        visited[node] = True
        cnt = 1

        for nxt in graph[node]:
            if not visited[nxt]:
                cnt += dfs(nxt)

        return cnt

    answer = float("inf")

    for a, b in wires:

        # 전선 제거
        graph[a].remove(b)
        graph[b].remove(a)

        visited = [False] * (n + 1)

        cnt = dfs(1)

        answer = min(answer, abs(cnt - (n - cnt)))

        # 원상복구
        graph[a].append(b)
        graph[b].append(a)

    return answer