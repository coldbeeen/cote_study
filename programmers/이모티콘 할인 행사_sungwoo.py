import sys
sys.setrecursionlimit(10**6)

def solution(users, emoticons):

    def permutation(iter):  # 이모티콘 할인율에 대해 순열을 생성하는 함수

        if iter == len(emoticons):  # 순열이 완성되었다면 service_and_price_calc() 함수 호출 후 리턴
            service_and_price_calc()
            return

        for i in range(len(discount_rate)):  # iter가 이모티콘 개수와 일치할 때까지 할인율 값를 추가(append)해가며 순열을 만들어 나감
            emoticons_rate.append(discount_rate[i])
            permutation(iter+1)
            emoticons_rate.pop()

    def service_and_price_calc():  # 생성된 '이모티콘 할인율 순열'에 대해 '서비스 가입자' 및 '구매 비용'을 계산하는 함수

        nonlocal max_service, max_price
        service_result, price_result = 0, 0

        for i in range(len(users)):  # 모든 user 순회
            rate, price = users[i]
            price_sum = 0

            for j in range(len(emoticons)):  # (생성된 순열에 기반해) 할인율을 적용한 가격을 구한 뒤, 해당 user의 service 가입 여부 또는 구매 비용을 계산
                if rate <= emoticons_rate[j]:  # 할인율이 같거나 큰 경우 구매
                    price_sum += int(emoticons[j] - emoticons[j] * (emoticons_rate[j] / 100))

            if price_sum >= price:  # 이모티콘 구매 비용이 사용자가 원하는 가격 이상이라면 서비스를 가입
                service_result += 1
            else:  # 그렇지 않은 경우 이모티콘을 구매 (구매 비용 누적)
                price_result += price_sum

        if service_result > max_service:  # 서비스 가입자 업데이트 (1번 목표를 달성하기 위한 조건)
            max_service, max_price = service_result, price_result
        elif service_result == max_service and price_result > max_price:  # 같은 서비스 가입자에 대해 구매 비용 업데이트
            max_price = price_result


    max_service, max_price = 0, 0  # 최종 '이모티콘 플러스 서비스 가입 수'와 '이모티콘 매출액'을 담기 위한 변수 생성
    discount_rate = (10, 20, 30, 40)  # 할인율 후보

    emoticons_rate = []
    permutation(0)  # 이모티콘 할인율 순열을 생성함

    return [max_service, max_price]  # 최종 결과 리턴