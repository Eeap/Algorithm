import sys
input=sys.stdin.readline
n,m = map(int,input().split())
ary = [list(input()) for _ in range(n)]
dx=[1,0,0,-1]
dy=[0,1,-1,0]
visited = [[0 for _ in range(m)] for __ in range(n)]
result=[]
def dfs(x,y,prex,prey,cnt):
    if visited[x][y] and cnt >=4:
        result.append("yes")
        return
    visited[x][y]=1
    for idx in range(4):
        nx = dx[idx]+x
        ny = dy[idx]+y
        if 0<=nx<n and 0<=ny<m and ary[nx][ny]==ary[x][y]:
            if [nx,ny]!=[prex,prey]:
                dfs(nx,ny,x,y,cnt+1)


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j,i,j,0)
if result:
    print("Yes")
else:
    print("No")