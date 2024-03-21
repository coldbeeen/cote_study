#구글링
import sys

input = sys.stdin.readline

board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB") #replace 메소드로 간단하게 특정 문자를 대체할 수 있음

if 'X' in board:
    print(-1)
else:
    print(board)