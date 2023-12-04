import sys
from bisect import bisect_left

input = sys.stdin.readline

N, M = map(int, input().split())

power = [] #전투력
title = [] #칭호

for _ in range(N):
    name, num = input().split()
    title.append(name)
    power.append(int(num))

for _ in range(M):
    character = int(input())
    idx = bisect_left(power, character)
    print(title[idx])
    
#1. 입력받고 전투력에 대해 정렬이 필요할 것 같다고 생각함
#2. 근데 전투력이랑 칭호가 순서쌍에 맞게 같이 정렬되어야됨
#3. 그래서 딕셔너리로 key, value 묶어서 value 기준으로 정렬 시켰었음 -> game_dict = dict(sorted(game_dict.items(), key = lambda x: x[1]))
#4. 그리고 key 따로 value 따로 값 뽑아서 리스트로 만들고 칭호, 전투력으로 구분
#4. 정렬한거 bisect_left 써서 나온 인덱스를 칭호 리스트에서 출력시키니 예제대로 다 잘 나옴
#5. 제출했더니 3%에서 틀림
#6. 정렬이 필요없나 싶어서 정렬 코드빼고 돌리니까 IndexError 발생
#7. 나처럼 bisect_left 쓴 사람 블로그 보니 정렬도 안 시켰고 딕셔너리도 안 썼음
#8. 그래서 리스트 2개 만들어서 각각 입력받고 정렬도 안 시키고 bisect_left에 넣어봄
#9. 정답처리됨 ㅋㅋㅋㅋㅋㅋ
#10. 딕셔너리로 저장한 게 문제였던건지, keys()와 values()로 뽑은 값들이 입력부터 리스트에 저장할 때랑 다른건지 모르겠음
#11. 결론 : 너무 허무하고, 입력 자료형? 이슈때문에 이틀 날려먹은 게 너무 화난다