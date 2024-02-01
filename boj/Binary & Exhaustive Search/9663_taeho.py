n = int(input())

ans = 0
row = [0] * n

def is_promising(x): # 해당 위치에 퀸을 놓을 수 있는지
    for i in range(x):
        # 같은 열에 다른 퀸이 있거나, 양쪽 대각선에 다른 퀸이 있는 경우
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            row[x] = i # 퀸의 위치: [x, i]
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)