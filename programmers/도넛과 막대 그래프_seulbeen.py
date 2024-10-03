#도넛 : 나머지에서 뺴기
#막대 : 나가는거 1개 들어오는거 0개 or 나가는거 0개 들어오는거 1개
#8자 : 나가는거 2개 들어오는거 2개이상
#생성 정점 : 나가는 엣지밖에 없다? 근데 최소 2개 이상
from collections import defaultdict

def solution(edges):
    answer = [0,0,0,0]
    graph=defaultdict(list)
    graph_in=defaultdict(list)
        
    for e in edges:
        graph[e[0]].append(e[1])
        graph_in[e[1]].append(e[0])

    for g in graph:
        if len(graph[g])>=2 and g not in graph_in:
            mid=g
            answer[0]=mid
        if len(graph[g])==2 and len(graph_in[g])>=2:
            answer[3]+=1
        if len(graph[g])==1 and g not in graph_in:
            answer[2]+=1
    for g in graph_in:
        if len(graph_in[g])==1 and g not in graph:
            answer[2]+=1
    answer[1]=len(graph[mid])-answer[2]-answer[3]

        
        
            
    return answer