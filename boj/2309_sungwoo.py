import sys
input = sys.stdin.readline

heights = [int(input()) for i in range(9)]
sumOfHeights = sum(heights)

# 다른 사람 풀이 참고함
# 조합을 만들 대상으로 반복문을 짜면 매우 길어지므로
# 조합에서 제외할 대상으로 반복문을 짜서 풀이함
for h1 in range(len(heights)-1):
    for h2 in range(h1+1, len(heights)):
        if sumOfHeights - heights[h1] - heights[h2] == 100:  # 총합에서 조합에서 제외할 대상을 뺴서 100인지 검사
            result = [heights[i] for i in range(len(heights)) if i not in (h1, h2)]  # h1과 h2를 제외한 요소를 리스트로
            break

for i in sorted(result): print(i)  # 정렬해 출력