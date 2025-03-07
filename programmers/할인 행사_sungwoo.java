// 풀이 시간: 18분
// 풀이 방법: discount 원소를 한 칸씩 순회하며 discount 품목 및 수량 업데이트함
// (동시에 원하는 품목 조건 충족하는지 확인)

import java.util.*;

class Solution {

    // 원하는 조건을 만족하는지 확인하는 메서드
    public boolean isSatisfied(HashMap<String, Integer> discountMap, String[] want, int[] number) {

        for (int j = 0; j < want.length; j++)  // want와 number 체크
            if (discountMap.getOrDefault(want[j], 0) < number[j])  // 원하는 조건을 하나라도 만족하지 않는다면
                return false;

        return true;
    }

    public int solution(String[] want, int[] number, String[] discount) {

        HashMap<String, Integer> discountMap = new HashMap<>();  // 할인 품목/수량 Map 생성
        int answer = 0;

        for (int i = 0; i < discount.length; i++)  {  // 할인 품목을 업데이트하면서 원하는 조건을 모두 만족하는지 확인해나감

            if (i >= 10)  // 첫 10개 이후의 품목부터 '10일 전 품목 삭제 작업' 수행
                discountMap.put(discount[i - 10], discountMap.get(discount[i - 10]) - 1);  // 10일 전의 할인 품목 1개 삭제

            discountMap.put(discount[i], discountMap.getOrDefault(discount[i], 0) + 1);  // 이번 할인 품목 1개 추가

            if(i >= 9 && isSatisfied(discountMap, want, number))  // 원하는 조건을 만족한다면 answer 증가
                answer++;
        }

        return answer;
    }
}