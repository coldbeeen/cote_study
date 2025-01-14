// 풀이 시간: 18분

import java.util.*;

class Solution {
    public int[] solution(String[] operations) {

        LinkedList<Integer> list = new LinkedList<>();  // 링크드리스트 생성 (빠른 삽입/삭제)

        for (String operation: operations) {

            char o = operation.charAt(0);  // 명령어
            Integer n = Integer.parseInt(operation.substring(2));  // 숫자

            if (o == 'I') {  // I: 삽입
                list.add(n);
                list.sort(null);  // 삽입 시마다 정렬 수행 -> 팀소트: 이미 정렬된 리스트에 대해 O(n)
            } else {  // D: 삭제
                if (list.isEmpty())  // 큐가 비었으면 무시
                    continue;

                if (n == -1)  // 최솟값 삭제
                    list.removeFirst();
                else  // 최댓값 삭제
                    list.removeLast();
            }
        }

        if (list.isEmpty())  // 비어있으면 [0,0] 리턴
            return new int[]{0, 0};

        return new int[]{list.getLast(), list.getFirst()};  // [최댓값, 최솟값] 리턴
    }
}