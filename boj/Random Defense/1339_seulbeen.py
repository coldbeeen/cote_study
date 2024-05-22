import sys

input = sys.stdin.readline
N = int(input())

S = [input().strip() for _ in range(N)]
words = {}  # 단어별 값을 지정
for s in S:
    x = len(s) - 1  # 10의 x승(자릿수)
    for i in s:
        if i in words:
            words[i] += 10**x
        else:
            words[i] = 10**x
        x -= 1

words_sort = sorted(words.values(), reverse=True)  # 내림차순 정렬(9부터 내려와야댐)
result = 0
num = 9
for k in words_sort:
    result += k * num
    num -= 1
print(result)
