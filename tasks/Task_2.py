def is_valid(board):
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i][0] == board[j][0] or board[i][1] == board[j][1]:
                return False

    for i in range(8):
        for j in range(i + 1, 8):
            if abs(board[i][0] - board[j][0]) == abs(board[i][1] - board[j][1]):
                return False

    return True


queens = []
for _ in range(8):
    x, y = map(int, input().split())
    queens.append((x, y))

valid = is_valid(queens)

if valid:
    print("True")
else:
    print("False")
