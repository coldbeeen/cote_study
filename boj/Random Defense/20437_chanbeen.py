#80분 +@, 구글링

from collections import defaultdict

T = int(input())

for _ in range(T):
    W = input().rstrip()
    K = int(input())

    char_dict = defaultdict(list) #value 자료형 : 리스트

    for i in range(len(W)):
        if W.count(W[i]) >= K: #문자열 내 알파벳 개수가 K개 이상일 때만
            char_dict[W[i]].append(i) #알파벳이 등장한 인덱스를 value에 저장

    if char_dict:
        result = []

        for char_idx_list in char_dict.values():
            for i in range(len(char_idx_list) - K + 1): #문자열 내 K개씩 등장해야 하므로 
                result.append(char_idx_list[i + K - 1] - char_idx_list[i] + 1) #K개 등장했을 때 연속 문자열 길이

        print(min(result), max(result))
    else: #문자열 내 K개 이상인 알파벳이 없으면 -1 출력
        print(-1)

#딕셔너리 자료 구조 활용 문제
#value에 리스트를 두고, key 알파벳이 등장한 인덱스를 value의 요소로 저장
#이후 각 key(알파벳)마다 가지는 리스트를 순회하면서 같은 알파벳의 시작과 끝의 차이를 계산(연속 문자열의 길이)
#연속 문자열 길이가 가장 작은건 3번, 가장 큰건 4번 이므로 각각 출력

#딕셔너리에 인덱스를 리스트 형태로 저장하는 방식으로 접근해야 했던 인상적인 문제