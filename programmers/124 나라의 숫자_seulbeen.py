# 65분
# 제일 쉬워보였는데 제일 빡셌음
# 3진법으로 풀면될거같다 생각했지만 0,1,2로만 이루어진게 아니라 1,2,4로 이루어져있어서 뭔가 자꾸 안맞음

# 다른 경우는 일반 3진법하고 동일하지만, 나머지가 0인 경우에 3진법 변환이 문제요구대로 안 이루어짐
# 몫이 n, 나머지가 0일때 -> 몫을 n-1, 나머지가 3인 경우로 바꿔서 연산(어차피 수학적으로는 괴리 없음) -> 나중에 3을 4로 치환
def solution(n):
    answer = ""

    def convert(number):
        result = ""

        while number > 0:
            # 원래 3진법은 그냥 result+= number%3, number//=3 등으로 계산하면 되는데, 문제조건때문에 안됨

            #3으로 나눴을때 몫과 나머지
            divider = number // 3
            remainder = number % 3
            
            #나머지가 0인경우 몫을 -1해주고, 나머지를 3으로 만듦
            if remainder == 0:
                divider -= 1
                remainder = 3

            #결과에 나머지를 붙여주고, number=몫
            result += str(remainder)
            number = divider
        return result

    # 연산 시행후, 결과의 3을 모두 4로 치환
    answer = convert(n)
    answer = answer.replace("3", "4")
    print(answer[::-1])

    #결과값을 거꾸로 반환해야 n진법 수가 됨
    return answer[::-1]
