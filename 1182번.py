import sys
cnt=[]
input=sys.stdin.readline
def recur(i,res,sum,s,n):
    if sum==s and len(res)>0:
        cnt.append(0)
    for idx in range(i,n):
        res.append(ary[idx])
        sum+=ary[idx]
        recur(idx+1,res,sum,s,n)
        res.pop()
        sum-=ary[idx]

n,s = map(int,input().split())
ary = list(map(int,input().split()))
recur(0,[],0,s,n)
print(len(cnt))
