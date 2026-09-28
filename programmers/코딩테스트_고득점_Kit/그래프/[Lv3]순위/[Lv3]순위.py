def solution(n, results):
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]

    for a, b in results:
        win[a].append(b)
        lose[b].append(a)

    answer = 0

    for player in range(1, n + 1):
        visited = [False] * (n + 1)
        stack = [player]
        win_count = 0
        
        while stack:
            current = stack.pop()
            for next_player in win[current]:
                if not visited[next_player]:
                    visited[next_player] = True
                    win_count += 1
                    stack.append(next_player)
        visited = [False] * (n + 1)
        stack = [player]
        lose_count = 0

        while stack:
            current = stack.pop()
            for next_player in lose[current]:
                if not visited[next_player]:
                    visited[next_player] = True
                    lose_count += 1
                    stack.append(next_player)
        if win_count + lose_count == n - 1:
            answer += 1

    return answer