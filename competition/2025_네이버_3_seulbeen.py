from itertools import combinations
from collections import defaultdict
def solution(fruit,k):

    flavor=len(fruit[0])
    result=set()
    # 몇번 몇번 음식 쓸지
    for cases in combinations(range(flavor),k):
        tmp = [0 for _ in range(flavor)]
        # 몇번
        for c in cases:
            for j in range(len(c)):
                if c[j]==1:
                    tmp[j]=1
        result.add(tmp)
    return len(result)
