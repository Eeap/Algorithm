# 붕대 감기 문제
def solution(bandage, health, attacks):
    answer = 0
    begin = 0
    end = 0
    hp = health
    for t, attack in attacks:
        end = t
        total = end - begin - 1
        cont = 0
        for cnt in range(1, total + 1):
            cont += 1
            hp += bandage[1]
            if cont == bandage[0]:
                hp += bandage[2]
                cont = 0

            if hp >= health:
                hp = health
                cont = 0
        begin = t
        hp -= attack
        if hp <= 0:
            return -1
    return hp