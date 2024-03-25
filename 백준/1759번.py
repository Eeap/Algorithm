import sys

input= sys.stdin.readline

l,c=map(int,input().split())
ary = list(input().split())
ary.sort()
temp = [0]*c
def recur(temp,a,b,cnt,res,item):
    for i in range(c):
        if cnt >= l:
            if a >= 1 and b >= 2:
                print(res)
            return
        if not temp[i] and item < ary[i]:
            if ary[i] in ['a','e','i','o','u']:
                temp[i]=1
                recur(temp,a+1,b,cnt+1,res+ary[i],ary[i])
                temp[i]=0
            else:
                temp[i]=1
                recur(temp,a,b+1,cnt+1,res+ary[i],ary[i])
                temp[i]=0


recur(temp,0,0,0,"",".")

