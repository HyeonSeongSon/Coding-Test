from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [False] * len(words)

    queue = deque()
    queue.append((begin, 0))

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt

        for i in range(len(words)):
            if visited[i]:
                continue

            diff = 0

            for a, b in zip(word, words[i]):
                if a != b:
                    diff += 1

            if diff == 1:
                visited[i] = True
                queue.append((words[i], cnt + 1))

    return 0