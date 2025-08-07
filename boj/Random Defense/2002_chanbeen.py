#약 52분 소요

N = int(input())

D = [input().rstrip() for _ in range(N)] #대근
Y = [input().rstrip() for _ in range(N)] #영식

idxs = []

for i in range(N):
    idxs.append(D.index(Y[i])) #나온 차 순서대로 들어왔을 때는 순서가 어땠는지에 대해 정보가 담긴 인덱스

cnt = 0

for i in range(N): #i번째 차가 추월했는지에 대한 검증
    for j in range(i, N):
        if idxs[i] > idxs[j]: #뒤 요소의 인덱스가 작다는건 뒤 차가 터널 진입 당시에 먼저 들어옴 = 추월했다는 뜻
         cnt += 1 #i번째 차는 추월한 차
         break

print(cnt)

#예시대로 다 나오지만, 3%에서 틀렸다
#3%에서 틀린 코드는 1차 반복문이었는데, 이럴 경우 직전/직후 차량과만 비교가 가능함
#2중 반복문으로 수정하여 i번째 차가 추월했는지 뒤에 등장한 모든 차와 비교하였더니 통과
#입력 제한 1000이므로, N^2 복잡도는 허용