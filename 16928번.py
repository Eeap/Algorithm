import sys
from collections import deque

input=sys.stdin.readline
n,m = map(int,input().split())
ladder={}
snake={}
for i in range(n):
    a,b = map(int,input().split())
    ladder[a]=b
for i in range(m):
    a, b = map(int, input().split())
    snake[a] = b

visited=[10000 for _ in range(101)]
visited[1]=0
check=[0 for _ in range(101)]
def bfs(visited):
    q = deque([1])
    check[1]=1
    while True:
        if not q:
            break
        num = q.popleft()
        check[num] = 1
        for c in range(6,0,-1):
            if num+c <=100 and not check[num+c]:
                n_num = num+c
                if n_num in ladder:
                    l_num = ladder[n_num]
                    if not check[l_num]:
                        visited[l_num]=min(visited[num]+1,visited[l_num])
                        q.append(l_num)
                        # print(num,n_num,l_num)
                    continue
                if n_num in snake:
                    s_num = snake[n_num]
                    if not check[s_num]:
                        visited[s_num]=min(visited[num]+1,visited[s_num])
                        q.append(s_num)
                        # print(num, n_num, s_num)
                    continue
                if visited[num]+1 < visited[n_num]:
                    visited[n_num]=min(visited[num]+1,visited[n_num])
                    q.append(n_num)



bfs(visited)
print(visited[100])