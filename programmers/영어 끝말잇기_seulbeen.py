from collections import defaultdict
def solution(n, words):

    answer = []
    people=defaultdict(int)
    used_words=defaultdict(int)

    last_letter=words[0][-1]
    people[0]+=1
    used_words[words[0]]+=1
    
    for i in range(1,len(words)):
        w=words[i]
        
        if w[0]!=last_letter: #현재 단어의 첫번째 글자가 이전 마지막 글자와 불일치
            # print(f'word :{words[i]} \nlast_letter : {last_letter}')
            # print("1 case")
            answer.extend(((i%n)+1,people[i%n]+1))
            return answer
        
        last_letter=w[-1]
        used_words[w]+=1
        people[i%n]+=1
        
        if used_words[w]>1:# 이미 나온적이 있는 단어를 또 말했을 경우
            # print("2 case")
            answer.extend(((i%n)+1,people[i%n]))
            return answer
        
        
        
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    answer.extend((0,0))
    return answer