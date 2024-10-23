def solution(msg):
    answer = []
    
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    dic = {}
    for i in range(len(alphabet)):
        dic[alphabet[i]] = i + 1 #사전 초기화
        
    while True:
        if msg in dic:
            answer.append(dic[msg])
            break
        
        for i in range(1, len(msg)):
            if msg[:i + 1] not in dic: #조합한 단어가 사전에 없다면
                answer.append(dic[msg[:i]]) #현재 글자 번호 출력
                
                dic[msg[:i + 1]] = len(dic) + 1 #새로 사전에 등록
                
                msg = msg[i:] #이전까지의 단어들은 모두 사전에 등록되었으니, 이후 인덱스부터 보도록 슬라이싱 후 for문 종료           
                break
    
    return answer

# 16번에서의 if문은 점점 길게 조합한 단어를 보면서 사전에 없을 경우 새로 등록해나가는 방식
# 'KA'는 있고 'KAO'는 없을 때, 'KA'를 출력하고 'KAO'는 사전에 등록한 뒤 msg를 'O'로 슬라이싱해주는 방식으로 진행됨
# 예시를 보고 코드로 구현하면 해결할 수 있었던 문제지만 무한 반복문과 종료 조건문을 생각하는 데 시간이 좀 소요됐음