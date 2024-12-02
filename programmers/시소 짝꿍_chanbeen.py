#80분 +@, 구글링
from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    
    for c in counter:
        if counter[c] > 0: #counter[counter 내에 없는 key] = 0
            #무게가 같은 경우
            answer += counter[c] * (counter[c] - 1) // 2 #nC2
            
            #무게가 다른 경우 : (2, 3), (2, 4), (3, 4)
            answer += counter[c] * counter[c * 3 / 2]
            answer += counter[c] * counter[c * 4 / 2]
            answer += counter[c] * counter[c * 4 / 3]
    
    return answer

#weights의 길이가 100,000까진데, combinations() 함수에 길이가 10만인 리스트가 들어가면 시간 초과 발생
#gcd 및 lcm 함수는 시간복잡도가 O(n)이라고 함

#combinations 함수를 쓰지 않고 O(n^2)보다 낮게 순회를 마치는 법?
#weights 정렬 후 인덱스 기준으로 이진 탐색? X 비교할 대상이 없음


#이후는 구글링 내용

#counter 함수를 활용해서 간단하게 푸는 방법 발견
#counter 함수 결과값 : 리스트 내 원소의 개수를 카운트 한 딕셔너리
#weights의 길이는 최대 10만이지만, 각 weight는 100에서 1000사이인 점을 활용

#무게가 같으면 어디 앉아도 되니까 무게 같은 n명 중 2명 순서 상관 없이 구성 (조합)

#무게가 다른데 시소 짝꿍이 될 수 있는 경우의 수는 3가지가 있음
#그래서 인덱싱할 때 곱셈과 나눗셈을 활용하여 각 경우의 수에 매칭되는 weight를 가지는 사람이 몇 명 있는지를 찾음
#그런데 (200, 300)인 경우의 수가 있을 때 200에서 answer += 1이 됐으면 300에서도 해당이 되지 않을까? 싶었다
#하지만 300 * 3 / 2  = 450 != 200
#그리고 450은 딕셔너리에 key로 없으므로 0을 반환하게 됨