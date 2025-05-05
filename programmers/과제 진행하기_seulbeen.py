# 1시간 30 후 구글링
"""
시간이 되면 과제 시작
진행중이던거 멈추고 새과제 시작
멈춰둔 과제가 여러개일때는 가장 최근에 멈춘 과제부터 -> 스택

새과제->가장 최근 멈춘 진행중이던과제-> 예전에 멈춘 진행중이던 과제
끝난 순으로 결과저장
배열은 시간순 정렬이라는 보장 없음!
"""
def solution(plans):
    answer = []

    # 분으로 변환해주는 함수
    def convert(time):
        try:
            h, m = time.split(":")
        except:
            return int(time)
        return int(h) * 60 + int(m)

    # 시간 -> int로 바꾼 후 정렬
    for p in plans:
        p[1] = convert(p[1])
        p[2] = convert(p[2])
    plans = sorted(plans, key=lambda x: x[1])

    cur_time = plans[0][1]
    stack = [plans[0]]

    for p in plans[1:]:
        # 지금 들어오는 과제 정보 (나중에 보니 시작시간빼고 안쓰는 변수였음)
        # n_sub, n_start, n_time = p[0], p[1], p[2]
        n_start= p[1]

        # 스택에 들어온 과제 정보를 순차 처리
        while stack:
            sub, start, time = stack.pop()
            
            # 현재 시간이 다음 과제 시작 전보다 앞섰다면 갱신
            if cur_time < start:
                cur_time = start
            end = time + cur_time
            # 다음 과제 시작시간 전까지 끝낼 수 있음
            if end <= n_start:
                cur_time = end
                answer.append(sub)

            # 다음 과제 시작 전까지 못끝냄
            else:
                cur_time = n_start
                stack.append([sub, start, end - n_start])
                break
        stack.append(p)
    #남아있는 과제 몰아서 진행
    while stack:
        sub, _, _ = stack.pop()
        answer.append(sub)

    """
    원래 내 로직은 사건의 개수를 나눠서 
    새 과제를 끝내고 시간이 남는 경우 -> 스택의 과제
    새 과제 시작 후 못 끝낸 경우 -> 스택에 저장
    스택의 과제 중에 또 새과제가 들어오는 경우 -> 스택에 저장
    스택의 과제 끝나고 시간이 남는 경우 -> 다음스택의 과제

    이런식이었는데, 풀이를 보니 스택에 새 과제와 기존 과제를 구분짓지 않고 담는게 킥인듯...
    어차피 새과제라면 시작시간에 맞춰 stack에 append할 것이고, 
    후입선출이니 가장 최근 진행중이던 과제보다 우선순위일테니까...

    """

    return answer
