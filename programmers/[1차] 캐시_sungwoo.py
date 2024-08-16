from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()  # 데크 사용

    # 모든 도시 순회
    for city in cities:

        city = city.lower()  # 소문자로 변환
        print(cache)

        if city not in cache:  # 해당 도시가 cache에 없다면 cache miss
            answer += 5
            cache.append(city)  # 캐시에 넣고
            if len(cache) > cacheSize:  # 캐시가 넘쳤다면
                cache.popleft()  # 가장 오래 사용되지 않은 맨 앞 요소 pop

        else:  # 해당 도시가 cache에 있다면 cache hit
            answer += 1
            cache.remove(city)  # 해당 도시를 기존 캐시에서 지우고
            cache.append(city)  # 맨 뒤에 다시 추가 (가장 최근 사용 캐시로)

    return answer