// 풀이 시간: 35분

import java.util.*;

class Solution {
    public int solution(int[] order) {

        Stack<Integer> subContainer = new Stack<>();  // 보조 컨테이너 벨트

        int num = 1, orderIdx;  // num: 상자 번호, orderIdx: order의 인덱스 (리턴값)
        boolean notFound;

        for (orderIdx = 0; orderIdx < order.length; orderIdx++) {

            if (num == order[orderIdx]) {  // 컨테이너 벨트에 있다면 다음 상자로
                num++;
            } else if (!subContainer.isEmpty() && subContainer.peek() == order[orderIdx]) {  // 보조 컨테이너 벨트에 있다면 pop만 수행
                subContainer.pop();
            } else {  // 찾을 수 없다면
                notFound = true;
                for (; num <= order.length; num++) {  // orderNum을 찾아나감
                    if (num == order[orderIdx]) {  // 찾았다면 다음 상자로
                        notFound = false;
                        num++;
                        break;
                    }
                    subContainer.push(num);  // 찾는 동안 subContainer에 적재함
                }

                if (notFound)  // 못 찾았다면 반복문 종료
                    break;
            }
        }

        return orderIdx;  // 마지막 order의 인덱스를 그대로 리턴
    }
}