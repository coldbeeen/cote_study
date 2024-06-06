n = int(input())
seq = sorted(list(map(int, input().split())))  # 정렬
x = int(input())

l, r = 0, n-1  # 왼쪽 / 오른쪽 포인터
result = 0

while l < r:  # 두 포인터가 같아질 때 까지
    if seq[l] + seq[r] < x:  # 두 수의 합이 x보다 작다면 더 작은 쪽인 l의 인덱스를 증가
        l += 1
    elif seq[l] + seq[r] > x:  # 두 수의 합이 x보다 크다면 더 크 쪽인 r의 인덱스를 감소
        r -= 1
    else:  # 두 수의 합이 x라면 result 증가 및 포인터 이동
        result += 1
        l += 1
        r -= 1

print(result)