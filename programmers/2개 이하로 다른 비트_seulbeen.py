# 39분
# 10^15 ->2진법 변환하면 50자리
# 처음에는 다 하나하나 변환해서 비교했는데 시간초과
# 규칙을 찾아서 풀었음
# 짝수-> 제일 마지막자리 수를 1로 바꾸면 됨(2^0승을 추가하는 거니 1증가)
# 홀수-> 두개의 비트까지 바꿀수 있으니 작은자리 순으로 탐색할때 가장 처음등장하는 0을 1로 바꾸고, 그전의 1을 0으로 바꾸면 됨
def solution(numbers):
    answer = []

    #이진법 변환
    def convert_2(n):
        result = ""
        while n > 0:
            result += str(n % 2)
            n //= 2
        result = result[::-1]
        result = result.rjust(50, "0")
        return result
    
    # 10진법 변환
    def convert_10(n):
        result = 0
        for i in range(len(n)):
            if n[i] == "1":
                result += 2 ** int(i)
        return result

    for n in numbers:
        #짝수면 그냥 +1해주면 1비트 바뀐 수임
        if n % 2 == 0:
            answer.append(n + 1)

        #홀수일 경우
        else:
            # 1011(11) -> 1101(13) -> 1110(14)->1111(16)
            # 1001(9) -> 1010(10)
            
            #2진법으로 변환후 뒤집어서 가장 처음 나오는 0을 1로, 그전의 1을 0으로 바꾸고 다시 10진법 변환
            tmp = convert_2(n)
            tmp = tmp[::-1]
            tmp = list(tmp)
            for i in range(len(tmp)):
                if tmp[i] == "0":
                    tmp[i] = "1"
                    tmp[i - 1] = "0"
                    break
            answer.append(convert_10(tmp))
    # 원래 코드
    # def check(c,n):
    #     cnt=0
    #     for i in range(50):
    #         if c[i]!=n[i]:
    #             cnt+=1
    #         if cnt>2:
    #             return False
    #     return True
    # for n in numbers:
    #     tmp_n=convert_2(n)
    #     for i in range(n+1,10**15+1):
    #         tmp_i=convert_2(i)
    #         if check(tmp_i,tmp_n):
    #             answer.append(i)
    #             break

    return answer
