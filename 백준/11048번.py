import sys
cnt=[]
input=sys.stdin.readline
n,m = map(int,input().split())
ary = [list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dx=[1,0,1]
dy=[0,1,1]
dp[0][0]=ary[0][0]
for i in range(n):
    for j in range(m):
        for idx in range(3):
            y=dy[idx]+j
            x=dx[idx]+i
            if 0<=y<m and 0<=x<n:
                dp[x][y]=max(dp[i][j]+ary[x][y],dp[x][y])

print(dp[n-1][m-1])
