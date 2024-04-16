def solution(files, backups):
    result = []
    visited = [0]*len(files)
    for start in backups:
        sum = 0
        idx = 0
        for i in range(len(files)):
            t,s = files[i]
            if t <= start and not visited[i]:
                visited[i]=1
                sum+=s
                idx = i
        cnt = 0
        for i in range(idx,len(files)):
            t,s = files[i]
            if start < t <= start+sum and not visited[i]:
                visited[i]=1
                cnt+=1
        result.append(cnt)
    return result
