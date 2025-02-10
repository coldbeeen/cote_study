#약 32분 소요

def solution(s):
    answer = []
    
    s = s[2:-2] #맨 끝 {{}} 잘라주기
    
    array = []
    
    for elem in s.split('},{'):
        array.append(list(map(int, elem.split(',')))) #각 요소별로 int 형태 리스트로 변환 후 append
    
    array.sort(key = len) #key를 len으로 지정해주면 배열 내 각 요소의 길이 순으로 정렬됨
    
    for i in array:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer

#중복 원소 존재 가능
#원소 순서 다르면 다른 튜플 (1, 3, 2) != (1, 2, 3)
#주어지는 입력은 중복되는 원소가 없는 튜플
#s길이 최대 100만 -> O(n^2) 알고리즘 사용 불가능할 듯
#리스트로 입력값을 변환한 뒤 길이 순으로 정렬하고, 고유값 등장 순서로 answer에 넣었더니 통과
#최악 약 360ms

#복잡도가 O(n^2)인 것 같은데 어떻게 통과가 된 것인지는 궁금