#약 20분 소요

num_list = list(input())

num_dict = {}

for i in range(10):
    num_dict[i] = 0
    
for i in range(len(num_list)):
    num_dict[int(num_list[i])] += 1
    
bigger = 6 if num_dict[6] > num_dict[9] else 9
smaller = 6 if num_dict[6] < num_dict[9] else 9

reuse = (num_dict[bigger] - num_dict[smaller]) // 2
num_dict[bigger] -= reuse
num_dict[smaller] += reuse

print(sorted(num_dict.values())[-1])

#입력 제한 100만 : O(n^2) 알고리즘 불가능
#숫자별 개수 딕셔너리에서 카운팅하고, 6과 9 중 더 큰 숫자의 여유분 나눠준 뒤 가장 큰 value return