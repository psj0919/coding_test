# 백준 10448 유레카 이론

# 문제: 자연수가 주어졌을 때, 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있는지 없는지를 판단해주는 프로그램을 만들어라. 단, 3개의 삼각수가 모두 달라야 할 필요는 없다.

# 조건
# Input : 프로그램은 표준입력을 사용한다. 테스트케이스의 개수는 입력의 첫 번째 줄에 주어진다. 각 테스트케이스는 한 줄에 자연수 K (3 ≤ K ≤ 1,000)가 하나씩 포함되어있는 T개의 라인으로 구성되어있다.
# Output : 프로그램은 표준출력을 사용한다. 각 테스트케이스에대해 정확히 한 라인을 출력한다. 만약 K가 정확히 3개의 삼각수의 합으로 표현될수 있다면 1을, 그렇지 않다면 0을 출력한다.

#알고리즘: 각 삼각수를 계산하고 3 수를 더하여 input의 값을 이루는지 확인 해야함.


import sys

num = int(input())
trg = []
finish = False
for i in range(1, 45):
    trg.append(int((i * (i+1)) // 2))

for _ in range(num):
    finish = False
    inp = int(input())
    for i in range(0, len(trg)):
        for j in range(0, len(trg)):
            for k in range(0, len(trg)):
                if (trg[i] + trg[j] + trg[k] == inp) and (trg[i] + trg[j] + trg[k] <= 1000):
                    print(1)
                    finish = True
            if finish:
                break
        if finish:
            break
    if finish==False:
        print(0)

