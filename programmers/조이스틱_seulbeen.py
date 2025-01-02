# 85분
# 반례 찾고 고치느라 좀 더티하게 푼 느낌...?
# 알파벳을 바꾸는 총 횟수는 정해져 있음
# 이동을 얼마나 효율적으로 하느냐를 찾아야 하는 문제
"""
    a를 0, 이외를 1이라고 하면
    sdfaaadas
    111000101
    이동의 방법은 3가지가 있는 듯
    1. 한번에 -> 방향 이동
    2. 반복문을 돌며 '반환점'을 정해주고, 0번째 부터 반환점까지(1) ,반환점부터 마지막까지(2) 나눠서 이동
    이떄, (1)먼저 하고 돌아와서 (2)를 실행 하는 법이 있고, (2) 먼저 하고 돌아와서 (1) 하는법으로 나누면 됨
    """


def solution(name):
    def A_inarow():
        # 반례 찾다가 끄트머리에 A가 연속으로 있는 경우를 고려 안해서 계산해줌
        cnt = 0
        if name[-1] == "A":
            for i in range(len(name) - 1, -1, -1):
                if name[i] == "A":
                    cnt += 1
                else:
                    return cnt
        return cnt

    def cal():
        # 알파벳을 맞추는데 필요한 총 횟수
        result = 0
        for n in name:
            # 다음 알파벳으로 옮기는게 빠른지, 이전알파벳으로(Z 방향으로 거꾸로) 옮기는게 빠른지 비교 후 계산
            if ord(n) - ord("A") < ord("Z") - ord(n) + 1:
                result += ord(n) - ord("A")
            else:
                result += ord("Z") - ord(n) + 1

        return result

    # 마지막에 연속된 A의 개수
    a_inarow = A_inarow()
    # 우선 answer에 "오른쪽으로 쭉 이동하는 경우" 를 넣어줌(이때 마지막에 연속된 A가 있다면 그만큼 덜 이동해도 됨)
    answer = min(len(name) - 1, len(name) - 1 - a_inarow)
    # 반환점의 위치를 i라고 하면
    for i in range(len(name) - 1):

        # 반환점 다음 글자들중, A가 아닌 애까지 이동(그 사이에 있는 A들은 들를 필요가 없음)
        for j in range(i + 1, len(name)):
            next = j
            if name[next] != "A":
                break
        # 맨 위 주석 조건문을 구현
        # min((1)먼저 하고 그만큼 돌아와서 (2),(2)먼저 하고 돌아와서(1))
        answer = min(
            answer,
            min(i + i + len(name) - next, len(name) - next + len(name) - next + i),
        )
    print(f"move : {answer}")
    print(f"letter change: {cal()}")

    # 이동횟수 + 변경횟수
    answer += cal()

    # 이게 좀 더티한 반례 수정인데,,, A밖에 없는 애들이 있는경우(아무것도 할 필요 없는 경우) 처음 answer가 음수가 됨
    if answer < 0:
        return 0

    return answer
