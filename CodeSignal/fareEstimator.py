def solution(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    result = []
    for i in range(len(cost_per_mile)):
        result.append(ride_time*cost_per_minute[i]+ride_distance*cost_per_mile[i])
    return result