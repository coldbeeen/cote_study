# 센서
# 2시간 후 로직 구글링 후 구현
"""
개인적으로 문제가 좀 헷갈림... 문제를 이해하는 데만 시간을 엄청 쓴듯
가로등설치? 문제처럼 고속도로의 센서 위에 좌우로 x만큼 커버를 쳐야 하는 것이 아니라,
고속도로에 센서들이 설치되어 있고, 각 기지국에서 "몇번부터 몇번까지의 센서를 맡을래?" 느낌이었음

1. 센서의 위치를 정렬 후 중복 제거
2. 인접센서와의 거리 차이를 담은 배열을 만들고, 오름차순으로 정렬
3. 가장 거리가 먼 센서(a,b)를 동일 기지국이 담당하면 손해이므로, 가장 먼 센서거리를 배열에서 제거
4. 길이 n인 배열에서 n-1개의 거리가 나오고, k-1개를 제외한 구간을 기지국끼리 각각 커버(기지국이 k개라면 구간은 K-1개)
5. n-1-(k-1) n-k개 구간 커버
"""
import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
sensors=sorted(list(set(map(int,input().split()))))
# print(sensors)
n=len(sensors)
distance=sorted([sensors[i+1]-sensors[i] for i in range(n-1)])
# print(distance)
print(sum(distance[:n-k]))

