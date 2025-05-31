// 풀이 시간: 10분
// 풀이 방법: 우선순위 큐(최대힙)를 활용해 작업량이 높은 순으로 1씩 처리함

import java.util.*;

class Solution {
    public long solution(int n, int[] works) {

        // 1. 우선순위 큐(최대힙) 생성
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int work: works)  // 우선순위 큐에 작업 추가
            pq.offer(work);

        // 2. 시간(n)이 만료되거나 남은 작업이 모두 0이 되기 전까지 1씩 작업 수행
        while (n > 0 && pq.peek() > 0) {
            pq.offer(pq.poll() - 1);  // 작업량 최댓값 1 감소
            n--;  // 시간 1 감소
        }

        // 3. 야근 피로도를 계산
        long answer = 0;
        for (int num: pq)
            answer += num*num;

        return answer;
    }
}