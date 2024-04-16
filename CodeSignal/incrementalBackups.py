def solution(lastBackupTime, changes):
    result = []
    for timestamp, idx in changes:
        if lastBackupTime < timestamp and idx not in result:
            result.append(idx)

    result.sort()
    return result
