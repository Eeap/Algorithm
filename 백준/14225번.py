import sys
cnt=[]
input=sys.stdin.readline
num = [0]*2000000
n = int(input())
ary = list(map(int,input().split()))
num=[0]*2000001
def solution(ary,n):
    for i in range(1 << n):
        subseq = []
        for j in range(n):
            if i & (1 << j):
                subseq.append(ary[j])

        if len(subseq)>0:
            num[sum(subseq)]=1

        print(subseq)

solution(ary,n)
for idx in range(1,2000001):
    if not num[idx]:
        print(idx)
        break
