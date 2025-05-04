
def find_index(bingo, num):
    for i in range(0, 5):
        for j in range(0, 5):
            if bingo[i][j] == num:
                return i, j



bingo = []
answer = []
for i in range(0, 10):
    row = list(map(int, input().split()))
    if i > 4:
        answer.append(row)
    else:
        bingo.append(row)

answer_count = 0


for i in range(0, 5):
    for j in range(0, 5):
        a, b = find_index(bingo, answer[i][j])
        bingo[a][b] = 0
        answer_count += 1

        count = 0

        for q in range(0, 5):
            col = []
            for k in range(0, 5):
                col.append(bingo[q][k])
            if sum(col) == 0:
                count += 1


        for q in range(0, 5):
            col = []
            for k in range(0, 5):
                col.append(bingo[k][q])
            if sum(col) == 0:
                count += 1

        col = []
        for e in range(0, 5):
            col.append(bingo[e][e])
        if sum(col) == 0:
            count += 1

        col = []
        for r in range(0, 5):
            col.append(bingo[r][4-r])
        if sum(col) == 0:
            count += 1

        if count >= 3:
            print(answer_count)
            exit()