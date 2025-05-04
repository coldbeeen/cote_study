# 1시간
# 유효하지 않은 구간이 주어질 때는 -1이라는 문제 조건을 못봤음...
"""
짝수면 /2
홀수면 *3 -1
정적분을 어떻게 할까?
사다리꼴 넓이의 합?

구간 설명이 좀 이상한거 같긴한데,, 그냥 n에 -b 를 더해서 하면 될듯
"""
from collections import defaultdict
def solution(k, ranges):
    answer = []

    # 원래 넓이 계산 함수를 만들었는데, 계산을 계속 하는 것이 아니라, 미리 구해놓고 꺼내 쓰는게 더 나을거 같음
    # def nerby(start,end):
    #     # if start>end:
    #     #     reverse=1
    #     #     start,end=end,start
    #     # else:
    #     #     reverse=0
    #     nerb=0
    #     for i in range(start,end):
    #         # if reverse:
    #             # print(y[i],y[i+1])
    #         nerb+=(y[i]+y[i+1])
    #     # return -(nerb/2) if reverse else nerb/2
    #     return nerb/2

    # 우박수열 및 우박수열을 만들때까지 필요한 계산횟수를 구하는 함수
    def wbak():
        result = [k]
        tmp = k
        cnt = 0
        while tmp > 1:
            if tmp % 2 == 0:
                tmp //= 2

            else:
                tmp *= 3
                tmp += 1
            result.append(tmp)
            cnt += 1
        # print(cnt,result)
        return cnt, result

    # x(횟수), y(우박수열까지 만드는 과정의 값들)
    x, y = wbak()
    
    # 한칸 별로 사다리꼴의 넓이를 구해서 저장할 딕셔너리
    store = defaultdict(int)

    # 딕셔너리에 넓이 계산
    for i in range(x):
        store[i] = (y[i] + y[i + 1]) / 2

    for r in ranges:

        #우리가 아는 정적분 구간으로 변환
        s = r[0]
        e = x + r[1]
        print(s, e)

        # 유효하지 않은 구간 처리
        if s > e:
            answer.append(-1)
            continue
        
        #구간에 해당하는 사다리꼴 넓이 합
        nerby = sum(store[i] for i in range(s, e))
        answer.append(nerby)
    return answer
