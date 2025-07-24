rank_dict = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 
              'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 
              'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

total_points = 0
total_grade = 0

for _ in range(20): #입력 길이 20줄로 고정
    sub, point, rank = map(str, input().strip().split())

    point = float(point)

    if rank != 'P': #P는 계산에서 아예 제외
        total_points += point #수강 학점
        total_grade += point * rank_dict[rank] #수강 학점 * 등급

print(total_grade / total_points)