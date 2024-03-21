import sys
input=sys.stdin.readline
a,p=map(int,input().split())

nums=[]
nums.append(a)
while True:
    idx=len(nums)-1
    tmp=str(nums[idx])
    total=0
    for n in tmp:
        mul=1
        for _ in range(p):
            mul*=int(n)
        total+=mul
    if total in nums:
        print(nums.index(total))
        break
    else:
        nums.append(total)
