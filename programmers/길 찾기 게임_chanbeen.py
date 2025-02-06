#90+@, 구글링  

import sys
sys.setrecursionlimit(10**6) #재귀문 사용 시 작성해줘야 런타임 에러 발생 x

L, R = 2, 3 #tree 딕셔너리의 value 중 2번째 인덱스가 왼쪽 자식, 3번째 인덱스가 오른쪽 자식

def pre_order(tree, idx): #전위 순회
    path = []
    
    if idx == 0:
        return path
    
    path.append(idx) #먼저 방문하는 idx부터 append하면 전위 순회
    
    path += pre_order(tree, tree[idx][L]) #재귀문은 독립적인 함수로 취급되어서, 각각의 반환값을 연결
    path += pre_order(tree, tree[idx][R])
    
    return path
    
def post_order(tree, idx): #후위 순회
    path = []
    
    if idx == 0:
        return path
    
    path += post_order(tree, tree[idx][L])
    path += post_order(tree, tree[idx][R])
    
    path.append(idx) #리프 노드 idx부터 append하면 후위 순회
    
    return path
    
def insert(tree, node, parent_idx):
    x, y, idx = node
    px, py, left, right = tree[parent_idx] #px, py : parent의 x, y
    
    if px < x: #오른쪽 자식
        if right != 0: #자식이 없는 노드까지 재귀 탐색
            insert(tree, node, right)
        else:
            tree[parent_idx][R] = idx
            tree[idx] = [x, y, 0, 0] #딕셔너리에 key, value 저장
    else: #왼쪽 자식
        if left != 0: #자식이 없는 노드까지 재귀 탐색
            insert(tree, node, left)
        else:
            tree[parent_idx][L] = idx
            tree[idx] = [x, y, 0, 0]

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1) #노드 번호
        
    sorted_info = sorted(nodeinfo, key = lambda x : x[1]) #y좌표 기준 정렬
    
    tree = {}
    
    root_x, root_y, root_idx = sorted_info.pop()
    tree[root_idx] = [root_x, root_y, 0, 0] #현재 노드 x좌표, 현재 노드 y좌표, 왼쪽 자식 인덱스, 오른쪽 자식 인덱스
    
    while sorted_info:
        node = sorted_info.pop()
        
        insert(tree, node, root_idx) #트리 구조 구현
        
    return [pre_order(tree, root_idx), post_order(tree, root_idx)]

#노드 V 기준
#왼쪽 서브트리의 x값은 V의 x값보다 작다
#오른쪽 서브트리의 x값은 V의 x값보다 크다
#y좌표가 가장 큰 노드가 루트 노드
#y좌표가 큰 순서로 진행하면서, 기준 노드의 왼쪽에 있을지 오른쪽에 있을지는 x좌표가 결정함
#그래프의 간선을 적절히 연결하는 것이 중요함
#전위 순회와 후위 순회는 재귀문으로 간단하게 구현 가능


#구글링
#그래프 제작에 실패하여 구글링
#딕셔너리 구조로 그래프를 구현하는 방법도 존재
#자료구조를 파이썬으로 구현할 줄 알면 레벨3 실력이라고 할 수 있을 듯
#딕셔너리 구조를 적극적으로 활용할 줄 안다면 이런 그래프도 구현하기 수월해짐