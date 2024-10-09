from collections import defaultdict

def solution(survey, choices):
    answer = ""
    mbti = ["RT", "CF", "JM", "AN"] #이미 사전순 정렬되어있음
    point = defaultdict(int)

    for i in range(len(survey)):
        pt = choices[i] - 4

        #동의 답변
        if pt > 0:
            c = survey[i][1]

        #비동의 답변
        elif pt < 0:
            c = survey[i][0]
            pt = -pt

        else:
            continue

        #해당 글자의 포인트 추가
        point[c] += pt

    for c in mbti:
        
        #두 유형을 검사하는데, 이미 사전순 정렬이므로, 크거나 같은 경우에 0번인덱스의 성격으로
        if point[c[0]] >= point[c[1]]:
            answer += c[0]
        else:
            answer += c[1]

    return answer
