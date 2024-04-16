def solution(city):
    global result
    n = len(city)
    result = []
    visited = [0] * n
    visited[0] = 1

    def dfs(city, visited, cnt, n, idx):
        global result
        if idx == n - 1:
            result.append(cnt)
            return
        for i in range(n):
            if city[idx][i] != -1 and not visited[i]:
                visited[i] = 1
                dfs(city, visited, cnt + city[idx][i], n, i)
                visited[i] = 0

    dfs(city, visited, 0, n, 0)
    return min(result)


