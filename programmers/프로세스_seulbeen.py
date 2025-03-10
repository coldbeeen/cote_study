# 20분
# abcd->bcda->cdab->c->d->a->b
from collections import deque


def solution(priorities, location):
    answer = 0
    prior = deque()

    # 초기 프로세스의 인덱스와 우선순위를 튜플로 저장
    for idx, p in enumerate(priorities):
        prior.append((idx, p))
    print(prior)
    
    #우선순위가 가장 높은 프로세스
    cur_max = max(prior, key=lambda x: x[1])
    
    while True:
        idx, p = prior.popleft()

        # pop한 프로세스의 우선순위가 더 높다면
        if cur_max[1] <= p:
            #프로세스 실행
            answer += 1
            
            # target 프로세스라면 answer 반환
            if idx == location:
                return answer
            # 남아있는 프로세스 중 최대우선순위 갱신
            cur_max = max(prior, key=lambda x: x[1])
        
        # 우선순위에 밀린 프로세스라면 다시 append
        else:
            prior.append((idx, p))
