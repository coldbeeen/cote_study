def check(l):
    for i in range(N - l + 1):
        for j in range(M - l + 1):
            if array[i][j] == array[i][j + l - 1] == array[i + l - 1][j] == array[i + l - 1][j + l - 1]:
                return True
        
    return False

N, M = map(int, input().split())

array = [list(map(int, list(input()))) for _ in range(N)]

length = min(N, M)

for i in range(length, 0, -1):
    if check(i):
        print(i ** 2)
        break
    
#정사각형을 찾는 문제
#N, M 중 더 작은 값까지로 크기 설정
#사이즈 줄여가면서 하나씩 인덱스 기반 체크