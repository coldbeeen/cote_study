from collections import defaultdict


def solution(msg):
    answer = []
    lzw = defaultdict(int)
    for i in range(26):
        lzw[chr(ord("A") + i)] = i + 1
    # 사전 구축

    letter = ""
    answer = [0]
    index = 26

    for i in range(len(msg)):
        # letter에 탐색할 글자추가
        letter += msg[i]

        # 그 글자가 사전에 없으면
        if not letter in lzw:
            # 사전의 다음 인덱스에 등록
            index += 1
            lzw[letter] = index

            # 탐색할 글자를 방금 그 글자로 초기화(다음 반복문에 여기에 이어붙일거니까)
            letter = msg[i]
            answer.append(lzw[letter])

        else:
            # 사전에 이 글자가 있으면 갱신
            answer[-1] = lzw[letter]

    return answer
