#약 36분 소요

def solution(numbers):
    answer = []
    
    for num in numbers:
        bin_num = list('0' + bin(num)[2:]) #3 -> ['0', '1' , '1']
        
        idx = ''.join(bin_num).rfind('0')
        
        bin_num[idx] = '1'
        
        if num % 2 == 1:
            bin_num[idx + 1] = '0'
        
        answer.append(int(''.join(bin_num), 2)) #011 -> 3
        
    return answer

#bin 함수 사용하면 2진수 반환, 3 -> '0b11' 로 나오므로 슬라이싱하여 사용
#비트가 1 ~ 2개 다른 수 중 가장 작은 수는 가장 오른쪽에 있는 0을 1로 바꾸는 것
#짝수인 경우에는 맨 오른쪽 비트가 0이므로 바로 해결됨
#홀수인 경우에는 맨 오른쪽 비트가 1이므로 추가 변환 필요
#홀수일 때는 가장 오른쪽에 있는 0을 찾고, 그 오른쪽에 있는 1을 0으로 바꿔주면 됨, 가장 큰 2진수를 없애는 원리
#그러면 x보다 크면서, 2개 이하로 다른 비트인 수 중 가장 작은 수 충족

#rfind까지는 금방 떠올렸지만, 짝수/홀수 로직을 떠올리는 데 시간을 좀 소비