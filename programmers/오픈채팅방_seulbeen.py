# 40분
# 들어오는거와 나가는 로그를 순서대로 기록해놓고, ID와 닉네임을 딕셔너리로 관리하자
# 생각해보니 로그 기록할때 deque가 아니라 일반 리스트였어도 됐을듯
from collections import defaultdict, deque


def solution(record):

    answer = []
    d = defaultdict(str)
    q = deque()

    def make_log(log):
        id, c = log[0], log[1]
        if c == "Enter":
            c = "들어왔습니다."
        else:
            c = "나갔습니다."
        # id에 해당하는 닉네임과 명령어를 기반으로 한 output 반환
        output = f"{d[id]}님이 {c}"
        return output

    for r in record:
        # Leave일 경우 name 없음
        if r[0] == "L":
            command, ID = r.split(" ")
        else:
            command, ID, name = r.split(" ")
        # 입장
        if command == "Enter":
            q.append((ID, command))
            d[ID] = name
        # 퇴장
        elif command == "Leave":
            q.append((ID, command))
        # 이름 변경
        else:
            d[ID] = name

    for i in q:
        answer.append(make_log(i))
    return answer
