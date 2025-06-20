#약 21분 소요

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

word_dict = {}

for _ in range(N):
    string = input().rstrip()

    if len(list(string)) >= M: #길이 M 이상만 딕셔너리로 관리
        if string in word_dict:
            word_dict[string] += 1
        else:
            word_dict[string] = 1

sorted_word_dict = sorted(word_dict.items(), key = lambda x : (-x[1], -len(x[0]), x))
#1순위 : 등장 횟수 많은 순, 2순위 : 단어 길이 긴 순, 3순위 : 사전 오름차순

for key, value in sorted_word_dict:
    print(key)