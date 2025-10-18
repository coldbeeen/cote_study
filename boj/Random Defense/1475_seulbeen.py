# 방 번호
# 21분
# Counter 써서 6,9 개수만 2로 나눠주면 될거 같다고 생각했는데, 굳이 그렇게 안해도 될것 같음

import sys
from collections import Counter
input=sys.stdin.readline

room_num=input().rstrip()
# print(room_num)
total=[0]*10

for i in room_num:
    check=int(i)
    # 숫자가 6이나 9인 경우에는 서로 땜빵이 가능하니 적은 쪽 숫자에 +1
    if check==6 or check==9:
        if total[6]<=total[9]:
            total[6]+=1
        else:
            total[9]+=1
    # 다른 숫자들은 필요할때마다 세트가 필요함
    else:
        total[check]+=1
        
        
print(max(total))
            
        
