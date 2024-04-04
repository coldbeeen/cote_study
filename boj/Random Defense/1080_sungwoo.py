def invert_3x3(matrix, i, j):  # 3x3 행렬을 반전시키는(뒤집는) 함수
    for k in range(i, i + 3):
        for l in range(j, j + 3):
            matrix[k][l] = 0 if matrix[k][l] else 1

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]

result = 0

for i in range(n-2):  # 입력받은 행렬에서 3x3 부분 행렬을 순회!
    for j in range(m-2):
        if a[i][j] != b[i][j]:  # 첫 번째 원소만 비교하여 다르다면 뒤집기! (결국 모든 원소를 순회하게 됨)
            invert_3x3(a, i, j)
            result += 1

flag = True
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:  # 모두 순회하는데 하나라도 다르다면 -1을 출력해야 함
            flag = False

print(result if flag else -1)