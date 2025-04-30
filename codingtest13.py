


N, M = map(int, input().split())
board = [['' for _ in range(M)] for _ in range(N)]
for j in range(0, N):
    row = list(input().strip())
    board[j] = row

max_area = 1

for i in range(N):
    for j in range(M):
        for l in range(1, min(N - i, M - j)):
            if board[i][j] == board[i][j+l] == board[i+l][j] == board[i+l][j+l]:
                max_area = max(max_area, (l+1)**2)

print(max_area)