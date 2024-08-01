# 구글링
# 건너뛰어야 하는 구간의 최대길이와 k일때 최대한 많은 인원이 건널 수 있음
# 1명씩 건너는 연산을 하는게 아니라 mid명을 건너게 한다는 로직
# mid를 return 해야 된다고 생각하는데 계속 틀려서 end도 리턴해보고 start도 리턴해보다가 얼떨결에 맞음

def solution(stones, k):

    start = 1
    end = 200000000

    while start <= end:

        mid = (start + end) // 2
        each_case = stones.copy()
        #건너뛰는 돌의 갯수 = cnt
        cnt = 0

        for i in range(len(each_case)):

            if each_case[i] <= mid:  # mid명을 건너게 했을때 건너뛰어야 하는 돌
                cnt += 1 #건너뛰는 돌의 개수 증가
            else:  # 밟고 지나갈 수 있는 돌
                #밟고 지나갈 수 있는 돌은 cnt=0
                cnt = 0

            if cnt == k:
                #반복문을 진행하다가 건너뛰어야 하는 돌의 개수가 k가 된다면 그게 최대 인원
                break

        print(f"start : {start} end : {end} mid : {mid}")
        print(f"cnt : {cnt}")
        print("-------------")

        if cnt == k:
            end = mid - 1

        else:
            start = mid + 1

    return start
