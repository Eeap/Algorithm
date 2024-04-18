def solution(dimensions, tasks, mouseCoordinates):
    w = dimensions[0]
    h = dimensions[1]
    s = dimensions[2]
    data = dict()
    sx = 0
    sy = 0
    y1 = mouseCoordinates[0][1]
    y2 = mouseCoordinates[1][1]
    if y1 > y2:
        temp = y1
        y1 = y2
        y2 = temp
    result = []
    for item in tasks:
        data[item] = [[sx, sy], [sx + w, sy + h]]
        for n in range(y1, y2 + 1):
            if sy <= n <= sy + h:
                result.append(item)
                break

        sy += h + s
    return result
