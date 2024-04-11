from collections import deque

a, b = map(int, input().split())
q = deque([a])  # 큐 활용 (초기값은 a로 설정)
dist = {a: 1}  # 연산 횟수를 담기 위해 딕셔너리 활용 (입력 범위가 매우 큰 관계로)

while q:  # BFS 수행
    n = q.popleft()

    if n == b:  # b를 찾은 경우 종료
        break
    if n > b:  # b보다 크다면 해당 수는 건너뜀
        continue

    n1, n2 = (n * 2, n * 10 + 1)  # 2를 곱한 값과 1를 붙인 값
    dist[n1] = dist[n2] = dist[n] + 1  # 연산 횟수 1 증가
    q.extend([n1, n2])  # 두 수를 큐에 추가

print(dist[b] if b in dist else -1)  # dist에 key로 존재한다면 값 출력, 없다면 못 만드는 것이므로 -1 출력