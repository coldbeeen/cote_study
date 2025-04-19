import heapq
from collections import defaultdict
import ast
def solution(request,n,a,b):
    result=[]
    t=0
    q=[]
    id_dict=defaultdict(int)
    for r in request:
        # 재접속
        if r[1] in id_dict:
            if r[0]-q[0]>b:
                q.remove(id_dict[r[1]])
                del id_dict[r[1]]
                result.append(len(q))
                continue
            
            q[q.index(id_dict[r[1]])] = r[0]
            id_dict[r[1]]=r[0]

            heapq.heapify(q)
            result.append(len(q))
            continue
        # 접속 가능
        if len(q)<n:
            heapq.heappush(q,r[0])
            id_dict[r[1]]=r[0]
            result.append(len(q))
        # 접속 불가능
        elif len(q)==n:
            # 자리비움 상태
            if r[0]-q[0]>=a:
                # 자리비움 쳐내기
                out=heapq.heappop(q)
                # del id_dict[out]
                id_dict={k:v for k,v in id_dict.items() if v==out}
                # 새로운애 추가
                heapq.heappush(q,r[0])
                id_dict[r[1]]=r[0]
                result.append(n)
            else:
                result.append(-1)


            # elif:
    print(q)
    return result

# tmp=[i for i in range(10,1,-1)]
# t=tmp.index(10)
# print(t)
request=input()
request=ast.literal_eval(request)
n,a,b=5,100,200
print(solution(request,n,a,b))
