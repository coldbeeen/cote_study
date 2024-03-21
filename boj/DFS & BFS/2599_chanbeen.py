import sys

input = sys.stdin.readline

N = int(input())

student = []

for _ in range(3):
    s = list(map(int, input().split()))
    student.append(s)

flag = 1
#구글링
for i in range(student[0][0] + 1): #0명도 가능, 모든 경우의 수 테스트위해 반복문 사용
    ab= i #A남학생 / B여학생
    ac = student[0][0] - ab #A남학생 / C여학생 : A남학생 수 - (A남학생 / B여학생 수)
    bc = student[2][1] - ac #B남학생 / C여학생 : C여학생 수 - (A남학생 / C여학생 수)
    ba = student[1][0] - bc #B남학생 / A여학생 : B남학생 수 - (B남학생 / C여학생 수)
    ca = student[0][1] - ba #C남학생 / A여학생 : A여학생 수 - (B남학생 / A여학생 수)
    cb = student[2][0] - ca #C남학생 / B여학생 : C남학생 수 - (C남학생 / A여학생 수)
    
    if ab >= 0 and ac >= 0 and bc >= 0 and ba >= 0 and ca >= 0 and cb >= 0:
        #0보다 작은 값이 있다면 만들어져야하는 짝꿍 수만큼 인원이 충분하지 않은 것, 경우의 수 성립 안 함
        print(flag)
        print(ab, ac)
        print(ba, bc)
        print(ca, cb)
        
        flag = 0
        break

if flag:
    print(0)