import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):  # i가 1~n을 순회하며
    if i + sum(map(int, list(str(i)))) == n:  # i의 분해합이 n이라면 출력 후 종료
        print(i)
        break
else:  # 위 break가 실행되지 않았다면 0 출력
    print(0)