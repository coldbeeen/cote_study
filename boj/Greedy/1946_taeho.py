# 서류 오름차순
# 면접 결과 기준으로, 서류 심사 내 윗 등수보다 등수가 높아야 함
# 서류 1등은 어차피 뽑히니까, 면접 2등부터 보면 되긴 함
import sys
input = sys.stdin.readline

T = int(input())     # 테스트 케이스

for i in range(T):
    N = int(input()) # 지원자 수
    rank = []        # 지원자 등수
    
    for j in range(N):
        rank.append(tuple(map(int, input().split())))
    
    rank.sort(key=lambda x:x[0])   # 서류 등수 기준으로 오름차순 정렬 # rank[서류등수-1][0=서류등수, 1=면접등수]
    comp_rank = rank[0][1]         # 면접 기준 등수(최초값은 서류 1등의 면접 등수)
    count = 1                      # 1등은 어차피 있으니, 1부터 시작
    
    for j in range(1, N):          # 서류 2등 인원부터 시작
        if rank[j][1] < comp_rank: # 어떤 지원자의 면접 등수가 서류 등수가 더 높은 지원자들의 가장 좋은 면접 등수보다 높을 경우
            count += 1             # 신입사원으로 적절, 1 추가
            comp_rank = rank[j][1] # 기준 등수를 변경
    
    print(count)