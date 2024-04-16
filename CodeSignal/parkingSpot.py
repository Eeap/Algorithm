def solution(carDimensions, parkingLot, luckySpot):
    x = abs(luckySpot[0] - luckySpot[2]) + 1
    y = abs(luckySpot[1] - luckySpot[3]) + 1
    if x == carDimensions[0] and y == carDimensions[1]:
        # 행이 길이와 같은 경우
        # 주차 자리 체크
        for i in range(luckySpot[0], luckySpot[2] + 1):
            for j in range(luckySpot[1], luckySpot[3] + 1):
                if parkingLot[i][j] == 1:
                    return False
        # 들어가는 입구 체크
        noEnt = False
        # 위 체크
        for j in range(luckySpot[1], luckySpot[3] + 1):
            for i in range(luckySpot[0] + 1):
                if parkingLot[i][j] == 1:
                    noEnt = True
        if not noEnt:
            return True
        noEnt = False
        # 아래 체크
        for j in range(luckySpot[1], luckySpot[3] + 1):
            for i in range(luckySpot[2] + 1, len(parkingLot)):
                if parkingLot[i][j] == 1:
                    noEnt = True
        if not noEnt:
            return True

    elif y == carDimensions[0] and x == carDimensions[1]:
        # 행이 넓이와 같은 경우
        # 주차 자리 체크
        for i in range(luckySpot[0], luckySpot[2] + 1):
            for j in range(luckySpot[1], luckySpot[3] + 1):
                if parkingLot[i][j] == 1:
                    return False
        # 들어가는 입구 체크
        noEnt = False
        # 왼쪽 체크
        for i in range(luckySpot[0], luckySpot[2] + 1):
            for j in range(luckySpot[1]):
                if parkingLot[i][j] == 1:
                    noEnt = True
        if not noEnt:
            return True
        noEnt = False
        # 오른쪽 체크
        for i in range(luckySpot[0], luckySpot[2] + 1):
            for j in range(luckySpot[3] + 1, len(parkingLot[0])):
                if parkingLot[i][j] == 1:
                    noEnt = True
        if not noEnt:
            return True

    return False
