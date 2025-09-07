#약 20분 소요

def count_color(x, y, n):
    global white, blue

    color = array[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if array[i][j] != color:
                count_color(x, y, n // 2) #2사분면
                count_color(x, y + n // 2, n // 2) #1사분면
                count_color(x + n // 2, y, n // 2) #3사분면
                count_color(x + n // 2, y + n // 2, n // 2) #4사분면
                return
    
    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())

array = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

count_color(0, 0, N)

print(white)
print(blue)

#한 정사각형 기준으로, 첫 인덱스를 color로 지정
#모든 인덱스가 같은 color가 아니라면, 해당 정사각형을 4개로 분할, 재귀문으로 재탐색
#정사각형 내 모든 인덱스가 같은 color가 될 때까지 분할
#white인지 blue인지 체크