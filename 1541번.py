import sys
input = sys.stdin.readline

inp = str(input())
outp=''
num=[]
op=[]
#op와 num 분리
for i in range(len(inp)):
    if inp[i] == '-':
        num.append(int(outp))
        outp=''
        op.append('-')
    elif inp[i] =='+':
        num.append(int(outp))
        outp = ''
        op.append("+")
    elif inp[i] =='\n':
        num.append(int(outp))
    else:
        outp+=inp[i]

res=[]
def recur(idx,numb):
    prev=numb
    for i in range(idx,len(op)):
        if op[i]=='-':
            res.append(prev)
            res.append("-")
            sum1=recur(i+1,num[i+1])
            return
        else:
            prev+=num[i+1]
    res.append(prev)
    return

recur(0,num[0])
sum=0
pass0=False
for i in range(len(res)):
    if res[i]=="-":
        sum-=res[i+1]
        pass0=True
    else:
        if pass0:
            pass0=False
            continue
        else:
            sum+=res[i]
print(res)
print(sum)