def solution(passcode, attempts):
    cnt = 0
    lock = False
    for at in attempts:
        if at == passcode:
            cnt = 0
        else:
            cnt+=1
        if cnt > 9:
            lock = True
            break
    return lock