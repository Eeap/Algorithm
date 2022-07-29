import sys

input= sys.stdin.readline
def recur(visited,i,cnt,res):
    if cnt==6:
        print(" ".join(map(str,res)))
        return
    for idx in range(i,k+1):
        if not visited[idx]:
            visited[idx]=1
            res.append(ary[idx])
            recur(visited,idx+1,cnt+1,res)
            res.pop()
            visited[idx]=0
while True:
    ary = list(map(int,input().split()))
    if ary[0]==0:
        break
    k=ary[0]
    visited=[0]*(k+1)
    recur(visited,1,0,[])
    print()
