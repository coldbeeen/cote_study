import sys

input = sys.stdin.readline

N = int(input())

words = [input().rstrip() for _ in range(N)]

word_dict = {}

for i in range(N):
    cnt = 1
    
    for j in range(len(words[i]) - 1, -1, -1):
        if words[i][j] not in word_dict.keys():
                word_dict[words[i][j]] = 0
        
        word_dict[words[i][j]] += cnt #문자별 몇 번 등장하는지 계산
        
        cnt *= 10 #자리수

sorted_by_cnt = sorted(list(word_dict.items()), key = lambda x: x[1], reverse = True)
#많이 등장한 알파벳 순서대로 정렬

num = 9

for i in range(len(sorted_by_cnt)):
    word_dict[sorted_by_cnt[i][0]] = num #많이 등장한 알파벳에게 큰 값 할당
    num -= 1

num_list = []

for i in range(N):
    tmp = ''
    
    for j in range(len(words[i])):
        tmp += str(word_dict[words[i][j]])
    
    num_list.append(int(tmp)) #문자를 숫자로 변환

print(sum(num_list))