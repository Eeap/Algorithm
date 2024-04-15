def solution(inputString, width):
    window = ""
    result = ""
    i = 0
    while i < len(inputString):
        compress = False
        for w in range(width, 0, -1):
            if i + w <= len(inputString):
                start = i - width
                end = i + width
                if start < 0:
                    start = 0
                if end > len(inputString) - 1:
                    end = len(inputString) - 1
                find_idx = int(window.find(inputString[i:i + w], start, end))
                if find_idx >= 0:
                    result += f"({find_idx},{w})"
                    window += inputString[find_idx:find_idx + w]
                    i += w
                    compress = True
                    break
        if not compress:
            result += inputString[i]
            window += inputString[i]
            i += 1
            # 하나만 치환
    return result