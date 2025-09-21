#약 20분 소요

N = int(input())

nums = list(map(int, input().split()))

array = [-1] * N   

stack = [0] #nums의 인덱스를 저장

for i in range(1, N):
    while stack and nums[stack[-1]] < nums[i]: #스택 : 후입선출
        array[stack.pop()] = nums[i] #오큰수 조건 성립하면 pop한 뒤 갱신
        
    stack.append(i)
    
print(*array)

#예전에 풀었던 오른쪽 가장 큰 수와 같은 로직의 문제
#i 인덱스의 수가 스택에 있는 인덱스의 수보다 크다면 오큰수 조건 성립
#스택 내 인덱스의 수와 i 인덱스의 수를 계속 비교, array 내 값 갱신
#리스트 앞에 * 붙이면 [] 출력 없이 요소만 출력됨