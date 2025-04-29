


N, M = map(int, input().split())
x = {"W":"B", "B":"W"}
board = [['' for _ in range(M)] for _ in range(N)]
for j in range(0, N):
    row = list(input().strip())
    board[j] = row

min1 = 0
min2 = 0
anw1 = [["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "B", "W", "B", "W", "B", "W", "B"], ["B", "W", "B", "W", "B", "W", "B", "W"]]

anw2 = [["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"],
        ["B", "W", "B", "W", "B", "W", "B", "W"], ["W", "B", "W", "B", "W", "B", "W", "B"]]

total = []

if N == 8 and M == 8:
    for k in range(0, 8):
        for l in range(0, 8):
            if anw1[k][l] != board[k][l]:
                min1 += 1

            if anw2[k][l] != board[k][l]:
                min2 += 1
    if min1 > min2:
        print(min2)
    else:
        print(min1)

else:
    for i in range(N-7):
        for j in range(M-7):
            for k in range(0, 8):
                for l in range(0, 8):
                    if anw1[k][l] !=board[i+k][j+l]:
                        min1 +=1

                    if anw2[k][l] !=board[i+k][j+l]:
                        min2 += 1

            total.append(min1)
            total.append(min2)
            min1, min2 = 0, 0

    print(min(total))