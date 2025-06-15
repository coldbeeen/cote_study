// 풀이 방법: '크기가 k인 구간'의 최댓값을 모두 구한다. 이후 최댓값 중에서 최솟값을 구한다. (슬라이딩 윈도우)

import java.util.*;

class Solution {
    public int solution(int[] stones, int k) {

        LinkedList<Integer> ll = new LinkedList<>();  // 인덱스를 저장할 연결 리스트 (맨 앞에 구간 내 최댓값이 오도록 할 것임)
        ArrayList<Integer> maxList = new ArrayList<>();  // 최

        for (int i = 0; i < stones.length; i++) {

            while (!ll.isEmpty() && stones[ll.getLast()] <= stones[i])  // 현재 값 이하의 값들은 모두 삭제 후
                ll.removeLast();

            ll.addLast(i);  // 현재 인덱스 추가!

            while (i - ll.getFirst() + 1 > k)  // k 구간 내에서 최댓값이 필요하므로, 첫 번째 요소(최댓값 인덱스)를 확인해 구간을 벗어난 인덱스라면 제거
                ll.removeFirst();

            if (i >= k - 1)  // k 구간이 시작되는 i부터 maxList에 추가함
                maxList.add(stones[ll.getFirst()]);
        }

        return Collections.min(maxList);  // 최솟값 리턴
    }
}