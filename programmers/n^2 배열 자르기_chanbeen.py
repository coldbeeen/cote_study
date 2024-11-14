#약 67분 소요

def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        q = i // n
        r = i % n
        
        if r == 0:
            answer.append(q + 1)
        elif r <= q:
            answer.append(q + 1)
        else:
            answer.append(r + 1)
    
    return answer

#대각 허용 bfs + extend 사용했으나 시간 초과
#extend 부분에서 시간 초과인 줄 알았으나 bfs에서 시간 초과 발생
#행렬로 bfs를 순회해서 O(n^2)가 되어 시간 초과인 듯

#dp처럼 1차원 행렬을 만들어 조건부로 채우려고 해봤으나 테스트 9, 10, 11에서 시간 초과 발생..
#반복문이 n * n번 동안 도는 것이니 사실상 얘도 O(n^2)

#배열을 다 채우지 말고, left에서 right 사이만 값을 구해볼까?

#몫과 나머지를 활용하여 인덱스 간 규칙을 발견하면, 간단히 풀리는 문제