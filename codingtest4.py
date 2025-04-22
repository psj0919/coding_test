def solution(bandage, health, attacks):
    answer = 0

    band_count = 0
    max_h = health
    attack_time = []
    damage = []
    for att in attacks:
        attack_time.append(att[0])
        damage.append(att[1])

    total_time = attacks[-1][0]

    for i in range(1, total_time+1):
        if max_h < health:
            band_count = 0
            health = max_h

        if i in attack_time:
            x = attack_time.index(i)
            dmg = damage[x]
            health = health - dmg
            band_count = 0
            if health <= 0:
                answer = -1
                return answer

        else:
            if max_h == health:
                band_count = 0
                pass
            else:
                if band_count != bandage[0]:
                    health += bandage[1]
                    band_count += 1
                    if bandage[0] == band_count:
                        health += bandage[2]
                        if health > max_h:
                            health = max_h
                        band_count = 0
                else:
                    band_count = 0


    answer = health

    return answer



if __name__=='__main__':
    print(solution([2, 1, 3], 20, [[1, 15], [6, 2]]))