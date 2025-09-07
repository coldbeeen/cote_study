#90분 +@, 구글링

s1 = list(input().rstrip())
s2 = list(input().rstrip())

lcs = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(max(map(max,lcs)))

#DP
#행렬에 저장되는 값 : s1의 i번째 문자, s2 j번째 문자에서의 LCS
#비교한 문자가 같을 경우 : 이전 LCS + 1
#비교한 문자가 다를 경우 : 이전 LCS 중 큰 값

#s1 : AC
#s2 : CAPCA
#라고 가정했을 때,

#이전 LCS 시나리오 
#1
#s1 : AC
#s2 : CAPC 까지의 LCS

#2
#s1 : A
#s2 : CAPCA 까지의 LCS

#1과 2중 더 큰 값을 현재 인덱스의 LCS로 갱신


#이해하는 데에도 1시간 걸린 문제