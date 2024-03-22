from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False]*(n+1)
    q = deque()
    for i in range(n):
        for j in range(n):
            if computers[i][j] and not visited[j]:
                q.append((i,j))
                answer+=1
            while q:
                x,y = q.popleft()
                visited[y]=True
                for idx in range(n):
                    if idx!=x and idx!=y and computers[y][idx] and not visited[idx]:
                        q.append((y,idx))
    return answer