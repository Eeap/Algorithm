def solution(l, fares):
    uber = ["UberX","UberXL","UberPlus","UberBlack","UberSUV"]
    for i in range(len(fares)-1,-1,-1):
        if fares[i]*l > 20:
            continue
        return uber[i]