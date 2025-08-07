# 시리얼 번호
# 23분
# 자릿수 합을 1번만 구하면 되는건데 한자리가 될때까지 구하는 줄 알았음...

"""
1. 짧은 순
2. 숫자 자리수 합 작은 순
3. 사전순
"""
n=int(input())

# 자릿수의 합을 구하는 함수
def digit_sum(code):
    numbers=[int(c) for c in code if c.isdigit()]
    num=sum(numbers)
    return num

# 시리얼 번호 입력
serial=[list(input().rstrip()) for _ in range(n)]

# 조건에 맞게 정렬
serial.sort(key=lambda x: (len(x),digit_sum(x),x))

# 출력
for i in range(n):
    for s in serial[i]:
        print(s,end="")
    print()




