# 석유 시추 문제
from collections import deque

def solution(land):
    answer = 0
    m = len(land)
    n = len(land[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    visited = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if land[i][j] == 1 and visited[i][j] == 0:
                oil = []
                q = deque()
                q.append((i, j))
                visited[i][j] = cnt
                while q:
                    x, y = q.popleft()
                    oil.append((x, y))
                    visited[x][y] = cnt
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if land[nx][ny] == 1 and visited[nx][ny] == 0:
                            # print(oil,nx,ny)
                            q.append((nx, ny))
                            visited[nx][ny] = cnt
                cnt += 1
                # 칸 채우기
                oil_cnt = len(oil)
                for x, y in oil:
                    land[x][y] = oil_cnt
    # result
    for col in range(n):
        result = 0
        result_list = []
        for row in range(m):
            if land[row][col] > 0 and visited[row][col] not in result_list:
                result_list.append(visited[row][col])
                result += land[row][col]
        if answer < result:
            answer = result

    return answer