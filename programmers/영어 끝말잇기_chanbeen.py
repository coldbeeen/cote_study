def solution(n, words):
    answer = [0, 0]

    word_dict = [words[0]]
    
    flag = 0
    
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1]: #끝말을 잇지 않을 때
            flag = 1
        
        if words[i] in word_dict: #단어 중복 사용
            flag = 1
        else:
            word_dict.append(words[i])
        
        if flag == 1: #같은 코드 여러번 쓰기 그래서 flag로 관리
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break

    return answer