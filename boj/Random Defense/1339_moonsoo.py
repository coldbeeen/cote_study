from collections import defaultdict

N = int(input())

char_to_int = defaultdict(int)
for i in range(N):
    # 문자열을 char 단위로 끊어주고 각 문자별로 딕셔너리에 기록합니다
    words = list(input())
    length = len(words)
    
    for i, char in enumerate(words):
        # char를 key로 하고 자릿수를 value로 하여 알파벳이 등장한 위치에서의 자릿수를 더해줍니다
        char_to_int[char] += 10 ** (length - i - 1)

# value 기준으로 내림차순 정렬합니다
char_to_int = sorted(char_to_int.items(), key = lambda item:item[1], reverse=True)

num = 9
result = 0
for key, value in char_to_int:
    # 9부터 차례대로 value와 곱하고 result에 더합니다
    # 알파벳은 최대 10개가 주어지기 때문에 음수가 나올 걱정은 하지 않아도 됩니다
    result += num * value
    num -= 1
    
print(result)