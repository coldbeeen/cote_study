import sys, math
input = sys.stdin.readline

n, nullfansyLen = map(int, input().split())

puddles = [list(map(int, input().split())) for i in range(n)]
puddles.sort(key=lambda x: x[0])  # 웅덩이 정렬

nullfansyIdx = -1  # 마지막 널빤지의 인덱스를 저장
nullfansyCnt = 0  # 최종 출력을 위한 널빤지 개수

for puddle in puddles:  # 웅덩이 순회

    if nullfansyIdx >= puddle[0]:  # 이전 널빤지가 현재 웅덩이를 침범했다면 해당 웅덩이의 기준을 널빤지가 끝난 다음 인덱스부터로 수정
        puddle[0] = nullfansyIdx + 1

    puddleLen = puddle[1] - puddle[0]  # 웅덩이 길이
    nullfansyUse = math.ceil(puddleLen / nullfansyLen)  # 사용할 널빤지의 개수
    nullfansyCnt += nullfansyUse
    nullfansyIdx = puddle[0] + nullfansyUse * nullfansyLen - 1  # 널빤지의 끝부분 인덱스를 저장

print(nullfansyCnt)