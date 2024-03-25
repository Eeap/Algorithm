import sys
cnt=[]
input=sys.stdin.readline
result = []
def recur(idx,visited,before_No,res):
    if idx==k:
        result.append(res)
        return

    for num in range(0,10):
        if idx==-1:
            visited[num]=1
            recur(idx+1,visited,num,res+str(num))
            visited[num]=0
        if not visited[num]:
           if compare[idx] == "<":
               if before_No < num:
                   visited[num]=1
                   recur(idx+1,visited,num,res+str(num))
                   visited[num]=0
               continue
           else:
               if before_No > num:
                   visited[num]=1
                   recur(idx+1,visited,num,res+str(num))
                   visited[num]=0
               continue

k = int(input())
compare = list(input().split())
recur(-1,[0]*10,-1,"")
print(result[len(result)-1],result[0])
