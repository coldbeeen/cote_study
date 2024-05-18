n = int(input())
word_list = [list(input()) for _ in range(n)]

# 모든 알파벳 붙인 후 중복 제거
alphabet_set = list(set([alphabet for alphabets in word_list for alphabet in alphabets]))
alphabet_score_dict = {}

# 모든 알파벳을 순회하며 score 생성 (A의 경우, ABCA -> 1001로 score가 계산됨)
for alphabet in alphabet_set:
    bit_list = [['0'] * len(alphabets) for alphabets in word_list]

    # word_list 순회하며 해당 알파벳 위치의 bit_list 비트값을 1로 변경
    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            if word_list[i][j] == alphabet:
                bit_list[i][j] = '1'

    # score 계산
    scores = [int(''.join(bit)) for bit in bit_list]
    alphabet_score_dict[alphabet] = sum(scores)

# score 내림차순 정렬
sorted_alphabet_score = sorted(list(alphabet_score_dict.items()), key = lambda x: x[1], reverse = True)

# word_list에 알파벳 내림차순으로 숫자 부여
number = 9
for alphabet_score in sorted_alphabet_score:
    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            if word_list[i][j] == alphabet_score[0]:
                word_list[i][j] = str(number)
    number -= 1

# 합하여 출력
result = sum([int(''.join(num)) for num in word_list])
print(result)