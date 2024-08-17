def solution(n, words):
    answer = [0, 0]
    previous = {words[0]}  # 이전에 등장했던 단어를 저장하기 위한 set

    # 2번째 단어부터 시작해 모든 단어를 순회
    for i in range(1, len(words)):

        # 이전 단어 마지막 문자와 일치하지 않거나, 등장했던 단어인 경우, answer 수정 후 break
        if words[i][0] != words[i-1][-1] or words[i] in previous:
            answer = [i % n + 1, i // n + 1]
            break

        previous.add(words[i])  # 등장한 단어 추가

    return answer