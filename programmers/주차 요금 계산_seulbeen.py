from collections import defaultdict


def solution(fees, records):

    # 시간을 정수로 변환하는 함수
    def transformer(time):
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)
    # 주어진 값을 바탕으로 요금을 계산하는 함수
    def cal_fee(parking_range):
        # 주차 시간이 기본요금 시간보다 작을경우 기본요금 반환
        if parking_range - fees[0] < 0:
            return fees[1]

        # 주석처럼 했는데 가독성 떨어지는듯
        # plus = ((parking_range - fees[0]) // fees[2] if (parking_range - fees[0]) % fees[2] == 0 else (parking_range - fees[0]) // fees[2] + 1)
        if (parking_range - fees[0]) % fees[2] == 0:
            #딱 단위요금으로 나눠떨어지는 경우
            plus = (parking_range - fees[0]) // fees[2]
        else:
            #아닐경우 올림처리
            plus = (parking_range - fees[0]) // fees[2] + 1
        #기본요금 + 추가요금 계산
        total = fees[1] + plus * fees[3]
        return total

    answer = []
    car_fee = defaultdict(list)
    total_car_fee = defaultdict(int)

    for r in records:
        time, car, flag = r.split(" ")
        #시간 정수로 변환
        time = transformer(time)
        if flag == "IN":
            #입차 : 입차시간 car_fee에 append
            car_fee[car].append(time)

        if flag == "OUT":
            #출차 : 입차했던 시간 pop 후 Total_car_fee에 누적 주차시간 더함
            in_time = car_fee[car].pop()
            time_gap = time - in_time
            total_car_fee[car] += time_gap

    
    for c, t in car_fee.items():
        #출차시간이 없을 경우(입차시간이 pop되지 않은 경우)
        if t:
            #23:59분에 출차했다고 가정하고 계산
            out_time = 23 * 60 + 59
            total_car_fee[c] += out_time - t[0]
    #주차요금 계산
    for c, f in total_car_fee.items():
        total_car_fee[c] = cal_fee(f)
    #차량번호순 정렬 후 answer에 append
    for c, f in sorted(total_car_fee.items()):
        answer.append(f)
    return answer
