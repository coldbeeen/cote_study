import sys
input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
nums.sort()
#정렬 해놓음

x=int(input())
cnt=0
#왼쪽 끝과 오른쪽 끝 인덱스 저장
left,right=0,len(nums)-1

while left < right:
    L=nums[left]
    R=nums[right]

    if L+R==x:
        #순서쌍 합이 x와 같다면 cnt증가, 인덱스 한칸씩 떙기기
        cnt+=1
        left+=1
        right-=1
    elif L+R>x:
        #x보다 크다면 오른쪽 인덱스를 한칸 땡겨서 합을 줄여야 함
        right-=1
    else:
        #x보다 작으면 왼쪽 인덱스 한칸 땡겨서 합을 늘림
        left+=1

print(cnt)
