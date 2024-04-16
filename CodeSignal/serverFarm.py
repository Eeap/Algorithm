def solution(jobs, servers):
    server_list = [0 for _ in range(servers)]
    result = [[] for _ in range(servers)]
    arr = dict()
    for i in range(len(jobs)):
        if jobs[i] in arr:
            arr[jobs[i]].append(i)
        else:
            arr[jobs[i]] = [i]
    arr = sorted(arr.items(),reverse=True)
    for key,lists in arr:
        lists.sort()
        for item in lists:
            idx = server_list.index(min(server_list))
            server_list[idx]+=key
            result[idx].append(item)
    return result

