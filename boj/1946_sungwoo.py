import sys
input = sys.stdin.readline

caseNum = int(input())

for case in range(caseNum):

    n = int(input())

    # 입력과 동시에 서류 순위로 정렬
    sortedByDocRankList = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: x[0])

    result = 0
    minInterviewRank = n + 1  # 인터뷰 순위 관리 (초깃값)
    for rank in sortedByDocRankList:
        # 서류 순위 정렬 리스트를 순회하면서 인터뷰 순위가 이전에 나온 인터뷰 순위(minInterviewRank)보다 낮다면 선발 가능
        if rank[1] < minInterviewRank:
            minInterviewRank = rank[1]
            result += 1


    print(result)