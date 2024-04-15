def solution(emails):
    data = dict()
    result = dict()
    for email in emails:
        idx = email.find("@")
        word = email[idx + 1:]
        if word in data:
            score, gb = data[word]
            score += 20
            data[word] = [score, gb]
        else:
            data[word] = [20, 0]
    for key in data:
        score, gb = data[key]
        if score >= 500:
            gb = 3 + 8 + 15 + 25
        elif score >= 300:
            gb = 3 + 8 + 15
        elif score >= 200:
            gb = 3 + 8
        elif score >= 100:
            gb = 3
        else:
            gb = 0
        if gb in result:
            result[gb].append(key)
        else:
            result[gb] = [key]
    result = sorted(result.items(), reverse=True)
    answer = []
    for gb, lists in result:
        lists.sort()
        answer += lists
    return answer


