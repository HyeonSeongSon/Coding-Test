from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    queue = deque([(0, 0)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 밖이면 넘어감
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 아직 방문하지 않은 길
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    if maps[n-1][m-1] == 1:
        return -1

    return maps[n-1][m-1]