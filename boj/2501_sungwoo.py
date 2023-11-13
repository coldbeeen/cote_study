import sys
input = sys.stdin.readline

n, k = map(int, input().split())

for i in range(1, n+1):  # 1부터 n까지 순회
    if n % i == 0:  # 약수라면
        k -= 1  # k 1씩 감소
        if k == 0:  # k가 0이라면 (k번째 약수인 경우) i 출력
            print(i)
            break
else:  # 위 break가 실행되지 않았다면 0 출력
    print(0) 