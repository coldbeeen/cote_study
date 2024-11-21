# 51분
# 시키는대로 로직 짜면 시간초과가 뜨네...다른 로직이 필요
# solve함수에서 현재 레벨별 재시도 횟수를 저장하는 배열로 줄이고자 했는데 이걸로는 부족함

# 이진탐색으로 줄일수 있었음
def solution(diffs, times, limit):

    def solve(level):
        time = 0
        # 레벨에 따른 각 문제별 재시도 횟수 저장한 배열
        retry = [max(0, d - level) for d in diffs]

        for i in range(len(diffs)):
            #재시도
            time += retry[i] * (times[i - 1] + times[i])
            #해당 문제 풀기
            time += times[i]
            #중간에 리밋 초과하면 False
            if time > limit:
                return False

        # 리밋이랑 비교 후 bool값 반환
        if time > limit:
            return False
        return True

    l = 1
    r = max(diffs)

    while l <= r:
        if l == r:
            return l
        mid = (l + r) // 2
        print(f"l : {l}, mid : {mid}, r : {r}")
        # 문제를 풀 수 있으면 우측 값을 mid로 설정
        if solve(mid):
            r = mid
        # 문제를 못 풀면 l값을 mid+1로 설정(mid는 안풀리니까)
        else:
            l = mid + 1

    
    return mid
