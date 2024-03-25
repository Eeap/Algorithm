# dfs 풀이
def solution(maps):
    global answer
    answer = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    m = len(maps[0])
    n = len(maps)
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    def dfs(i, j, cnt, visited):
        global answer
        if i == (n - 1) and j == (m - 1):
            if answer < cnt and answer != -1:
                return
            answer = cnt
            return
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if x < 0 or y < 0 or x >= n or y >= m or visited[x][y] or not maps[x][y]:
                continue
            visited[x][y] = 1
            dfs(x, y, cnt + 1, visited)
            visited[x][y] = 0

    dfs(0, 0, 1, visited)

    return answer

## bfs 풀이
from collections import deque


def solution(maps):
    answer = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    m = len(maps[0])
    n = len(maps)
    q = deque()
    q.append((0, 0))
    visited = [[0] * m for _ in range(n)]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[x][y] = 1
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    if maps[n - 1][m - 1] > 1:
        answer = maps[n - 1][m - 1]
    return answer