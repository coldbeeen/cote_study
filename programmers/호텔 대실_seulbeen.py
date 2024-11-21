# 87분
# 테스트케이스 1번만 자꾸 안돼서 반례 찾다가 5-60분쓴 듯
from collections import deque


def solution(book_time):
    answer = 0

    def time_to_int(time):
        h, m = time.split(":")
        return int(h) * 60 + int(m)

    book_time_int = []

    for b in book_time:
        check_in = time_to_int(b[0])
        check_out = time_to_int(b[1])
        book_time_int.append([check_in, check_out])

    book_time_int = sorted(book_time_int, key=lambda x: x[0], reverse=True)
    print(book_time_int)
    q = deque()
    q.append(book_time_int.pop())
    while q:
        t = q.popleft()
        answer += 1
        for i in range(len(book_time_int) - 1, -1, -1):
            if book_time_int[i][0] >= t[1] + 10:
                t = book_time_int[i]
                book_time_int.pop(i)
        # 원래 코드는 입실시간 기준 오름차순 정렬 후 이거였는데, remove를 쓰니 인덱스 빵꾸가 나서, 내림차순 정렬 후, 거꾸로 탐색하며 pop 해줘야 빵꾸가 안나는 거였음
        #(pop 해줘도 어차피 거꾸로 탐색이니 다음 탐색할 인덱스는 변하지 않으니까)
        """
        for b in book_time_int:
             if b[0] >= t[1] + 10:
                 t = b
                 book_time_int.remove(b)
        """
        if book_time_int:
            q.append(book_time_int.pop())
    return answer
