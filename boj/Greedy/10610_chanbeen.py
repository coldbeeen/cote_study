import sys

input = sys.stdin.readline

num = list(map(int, input().strip()))
#strip : 백준 질문 게시판 참고했음
#sys.stdin.readline은 입력 끝에 \n까지 받으므로, 입력받은 정수를 분할해줄 때는 끝의 \n도 잘라줘야함

if 0 not in num: #0 없으면 암만 노력해도 30의 배수는 안 됨
    print(-1)
else:
    if sum(num) % 3 == 0: #30의 배수는 자릿수를 다 더하면 3의 배수 - 슬빈이형 아이디어 참고했음
        num.sort(reverse=True)
        print("".join(map(str, num))) #최댓값 : 내림차순 정렬 후 순서대로 출력
        #join함수 구글링하여 참고하였음
    else:
        print(-1)