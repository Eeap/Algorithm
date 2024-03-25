from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    q = deque()
    q.append((begin,answer))
    visited = []
    while q :
        cur, answer = q.popleft()
        if cur == target:
            break

        for word in words:
            if cur == word:
                continue
            else:
                cnt = 0
                for i in range(len(begin)):
                    if cur[i] == word[i]:
                        cnt +=1
                # 하나빼고 다 동일시
                if cnt == len(begin) -1 and word not in visited:
                    visited.append(word)
                    q.append([word,answer+1])
    return answer




solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])