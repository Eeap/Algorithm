import sys
from collections import deque
input=sys.stdin.readline
n,l,r = map(int,input().split())
ary =[list(map(int,input().split())) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
'''
먼저 사이클을 찾고 방문한 노드는 방문에 저장

'''
def print_ary(ary,n,cnt):
    for i in range(n):
        print(ary[i])
    print(cnt)
def bfs(startx,starty,visited):
    result={(startx,starty)}
    q=deque([[startx,starty]])
    while True:
        if not q:
            break
        X,Y = q.popleft()
        visited[X][Y]=1
        for idx in range(4):
            x=dx[idx]+X
            y=dy[idx]+Y
            if 0<=x<n and 0<=y<n and not visited[x][y]:
                if l<=abs(ary[x][y]-ary[X][Y])<=r:
                    visited[x][y]=1
                    q.append([x, y])
                    result.add((x,y))
    return result

res=[]
cnt=0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if not visited[i][j]:
                temp = bfs(i,j,visited)
                if len(temp)==1:
                    continue
                res.append(temp)
    # print(visited)
    #calc
    if len(res)==0:
        break
    for lists in res:
        sum=0
        for x,y in lists:
            sum+=ary[x][y]
        # print(lists,sum)
        sum=int(sum/len(lists))
        for x,y in lists:
            ary[x][y]=sum
    # print_ary(ary,n,cnt)
    res=[]

    cnt+=1

    # exit()


print(cnt)
# bfs(visited)
