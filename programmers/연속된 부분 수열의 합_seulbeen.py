# 대충 2시간 넘게 걸리고 힌트 봄
# 비내림차순 (다음항이 같거나 큼)
# 짧은거 -> 시작인덱스가 작은거
def solution(s, k):
    result = 0
    # 하나로 될때
    if k in s:
        return [s.index(k), s.index(k)]
    
    # 하나도 안될때
    # 비내림차순이므로 끝에서(가장 큰 값)부터 탐색해서 k 찾는게 가장 적은 원소로 해결 가능
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
        if result > k:
            result -= s.pop()

        if result == k:
            # 시작 인덱스가 가장 앞쪽인걸 찾아야 하는 경우는 같은 원소들이 있는 경우밖에 없음
            while i > 0 and s[i - 1] == s[-1]:
                #같은원소일때까지 쭉 땡김
                i -= 1
                s.pop()
            return [i, len(s) - 1]
