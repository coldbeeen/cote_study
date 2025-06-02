# 20분
def solution(numbers):
    answer = []

    def convert_2(num):
        # 2진수로 변환하는 함수
        # 단, 계산의 편의성을 위해 역순으로 반환
        # ex: 8 -> 0001 
        result = []
        while num > 0:
            result.append(str(num % 2))
            num //= 2
        # 문제에 주어진 최댓값을 이진수로 변환하면 50자리이므로, 50자리까지 채워줌
        result = result + ["0"] * (50 - len(result))
        return result

    for n in numbers:
        #짝수라면 +1을 return
        if n % 2 == 0:
            answer.append(n + 1)
        #홀수라면
        else:
            # 이진수로 변환
            bi = convert_2(n)

            # 가장 먼저 나오는 0의 인덱스를 찾음
            idx=bi.index('0')

            #가장 먼저 나온 0을 1로 바꿔주고, 그 전(작은)자리의 1을 0으로 바꿔줌
            bi[idx] = "1"
            bi[idx - 1] = "0"
            
            tmp = 0
            # 해당 2진수를 10진수로 변환한 후 answer에 append
            for i in range(len(bi)):
                if bi[i] == "1":
                    tmp += 2**i
            answer.append(tmp)

    return answer


"""
'비트가 2개 이하로 다르다'는 말은 홀/짝에 따른 경우임!
1.N이 짝수
    이진법으로 변환했을때, 가장 오른쪽 자리(2^0 자리)가 0이라는 뜻
    -> 이것을 1로 바꿔준다면, N보다 크고 비트가 1개 다른 수 중에서 가장 작은수
    즉, 짝수면 +1해서 return하면됨
2.N이 홀수
    가장 작은 자리부터 탐색하며, 제일 처음 나오는 0을 1로, 그 전의 1을 0으로
"""
