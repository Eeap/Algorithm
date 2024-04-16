import math

def solution(departure, destination):
    result = []
    # f, f
    dep_x = math.floor(departure[0])
    dep_y = math.floor(departure[1])
    dest_x = math.floor(destination[0])
    dest_y = math.floor(destination[1])
    result.append(abs(dep_x - departure[0]) + abs(dep_y - departure[1]) + abs(dest_x - destination[0]) + abs(
        dest_y - destination[1]) + abs(dest_x - dep_x) + abs(dest_y - dep_y))

    # f, c
    dep_x = math.floor(departure[0])
    dep_y = math.floor(departure[1])
    dest_x = math.ceil(destination[0])
    dest_y = math.ceil(destination[1])
    result.append(abs(dep_x - departure[0]) + abs(dep_y - departure[1]) + abs(dest_x - destination[0]) + abs(
        dest_y - destination[1]) + abs(dest_x - dep_x) + abs(dest_y - dep_y))

    # \c, f
    dep_x = math.ceil(departure[0])
    dep_y = math.ceil(departure[1])
    dest_x = math.floor(destination[0])
    dest_y = math.floor(destination[1])
    result.append(abs(dep_x - departure[0]) + abs(dep_y - departure[1]) + abs(dest_x - destination[0]) + abs(
        dest_y - destination[1]) + abs(dest_x - dep_x) + abs(dest_y - dep_y))

    # c, c
    dep_x = math.ceil(departure[0])
    dep_y = math.ceil(departure[1])
    dest_x = math.ceil(destination[0])
    dest_y = math.ceil(destination[1])
    result.append(abs(dep_x - departure[0]) + abs(dep_y - departure[1]) + abs(dest_x - destination[0]) + abs(
        dest_y - destination[1]) + abs(dest_x - dep_x) + abs(dest_y - dep_y))

    return min(result)