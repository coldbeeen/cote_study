import sys
input = sys.stdin.readline

board = input().strip()
result = ""

i = 0

while i < len(board):

    if board[i] == '.':  # .은 하나씩 추가
        result += '.'
        i += 1
    elif board[i:i+4].count('X') == 4:  # .이 아니고 XXXX면 AAAA 추가
        result += 'A'*4
        i += 4
    elif board[i:i+2].count('X') == 2:  # XXXX가 아니고 XX면 BB 추가
        result += 'B'*2
        i += 2
    else:  # 외에는 덮기 불가능
        result = -1
        break

print(result)
