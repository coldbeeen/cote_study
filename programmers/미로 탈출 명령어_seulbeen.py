
def solution(n, m, x, y, r, c, k):
    answer = ""
    dist = abs(x - r) + abs(y - c)
    #불능
    if dist > k or dist % 2 != k % 2:
        return "impossible"
    # 진짜 필요한 거리 뺴고 남은 잉여 거리
    k -= dist

    #아래로 꼭 가야하는 거리(필요시)
    if r > x:
        answer += "d" * (r - x)
    
    #이제 잉여 거리만큼 d 방향 이동할거임 
    cx = max(x, r)
    #d로 이동할거니까 나중에 u로 돌라와야됨 나중을 위해 저장
    up = 0
    
    #k가 남아있는 선에서 가장 밑으로 이동
    while k and cx < n:
        cx += 1
        up += 1
        k -= 2
        answer += "d"

    # l로 꼭 가야 하는 거리(필요시)
    if y > c:
        answer += "l" * (y - c)

    #이제 l만큼 잉여거리이동
    cy = min(y, c)
    right = 0
    while k and cy > 1:
        cy -= 1
        right += 1
        k -= 2
        answer += "l"

    #왼쪽 끝이면 rl반복,아니라면 사전순으로 이득인 lr반복
    flag = "lr" if cy > 1 else "rl"

    while k:
        k -= 2
        answer += flag

    # 나머지 이동
    if y < c:
        answer += "r" * (c - y)
    answer += "r" * right
    if x > r:
        answer += "u" * (x - r)
    answer += "u" * up
    return answer
